"""Create age for user column

Revision ID: 1215f46356e1
Revises: e4590f61d4aa
Create Date: 2025-03-06 11:26:09.192767

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1215f46356e1'
down_revision: Union[str, None] = 'e4590f61d4aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('users', sa.Column('age',sa.Integer(), nullable = True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('users', 'age')
