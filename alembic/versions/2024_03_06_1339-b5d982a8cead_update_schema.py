"""update schema

Revision ID: b5d982a8cead
Revises: 
Create Date: 2024-03-06 13:39:03.465672

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5d982a8cead'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('farmInspection', 'Comments', new_column_name='comments')
    op.alter_column('farmInspection', 'typeodPesticideUsed', new_column_name='typeOfPesticideUsed')


def downgrade() -> None:
    op.alter_column('farmInspection', 'comments', new_column_name='Comments')
    op.alter_column('farmInspection', 'typeOfPesticideUsed', new_column_name='typeodPesticideUsed')
