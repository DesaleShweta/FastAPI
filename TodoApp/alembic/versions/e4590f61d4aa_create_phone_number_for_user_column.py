"""Create phone number for user column

Revision ID: e4590f61d4aa
Revises: 
Create Date: 2025-03-05 13:10:18.163075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4590f61d4aa'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('phone_number',sa.String(), nullable = True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'phone_number')
