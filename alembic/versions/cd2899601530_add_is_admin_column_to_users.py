"""Add is_admin column to users

Revision ID: cd2899601530
Revises: 1ac4c99bfdc0
Create Date: 2025-03-11 14:30:44.536540

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'cd2899601530'
down_revision: Union[str, None] = '1ac4c99bfdc0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Using batch mode to modify constraints safely in SQLite
    with op.batch_alter_table("movies") as batch_op:
        batch_op.add_column(sa.Column('category_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_category_id', 'categories', ['category_id'], ['id'])

    with op.batch_alter_table("users") as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))

def downgrade() -> None:
    # Using batch mode for rollback
    with op.batch_alter_table("users") as batch_op:
        batch_op.drop_column('is_admin')

    with op.batch_alter_table("movies") as batch_op:
        batch_op.drop_constraint('fk_category_id', type_='foreignkey')
        batch_op.drop_column('category_id')