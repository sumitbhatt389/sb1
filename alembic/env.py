from __future__ import with_statement
import logging
from logging.config import fileConfig

from sqlalchemy import create_engine
from sqlalchemy import pool
from sqlalchemy.ext.declarative import declarative_base
from alembic import context

# Import your models and metadata here
from models import Base  # Import the Base object
from models import Movie, Review  # Import your models if needed

# This is the Alembic Config object, which provides access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# Access the database URL and create engine
target_metadata = Base.metadata  # Set target_metadata to the metadata of your Base

# Other setup code ...

def run_migrations_online():
    # Connection and engine setup ...
    engine = create_engine(config.get_main_option("sqlalchemy.url"))
    connection = engine.connect()
    context.configure(
        connection=connection,
        target_metadata=target_metadata,  # Important: Provide metadata
    )

    with context.begin_transaction():
        context.run_migrations()

if context.is_offline_mode():
    # Offline migration setup...
    pass
else:
    # Online migration setup
    run_migrations_online()
