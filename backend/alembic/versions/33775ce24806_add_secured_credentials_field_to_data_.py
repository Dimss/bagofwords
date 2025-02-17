"""add secured credentials field to data_soure

Revision ID: 33775ce24806
Revises: 0996f318acf1
Create Date: 2024-12-02 20:17:18.353178

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33775ce24806'
down_revision: Union[str, None] = '0996f318acf1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data_sources', schema=None) as batch_op:
        batch_op.add_column(sa.Column('credentials', sa.Text(), nullable=True))

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('data_sources', schema=None) as batch_op:
        batch_op.drop_column('credentials')

    # ### end Alembic commands ###
