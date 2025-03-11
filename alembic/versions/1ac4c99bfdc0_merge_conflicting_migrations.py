"""Merge conflicting migrations

Revision ID: 1ac4c99bfdc0
Revises: 8c1ece038cf0, 92ba26263389
Create Date: 2025-03-11 14:28:45.241506

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ac4c99bfdc0'
down_revision: Union[str, None] = ('8c1ece038cf0', '92ba26263389')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
