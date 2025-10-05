"""Create favourite field in Todo Column

Revision ID: 586bb15ac091
Revises: 
Create Date: 2025-10-04 23:53:45.713665

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '586bb15ac091'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        table_name="todos",
        column=sa.Column('favourite',sa.Boolean,default=False,nullable=True)
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
