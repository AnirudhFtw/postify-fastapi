"""creat column content in posts

Revision ID: 84e72ec00d65
Revises: 2bafc1d93f80
Create Date: 2026-04-03 15:57:31.782013

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84e72ec00d65'
down_revision: Union[str, Sequence[str], None] = '2bafc1d93f80'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content' , sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
