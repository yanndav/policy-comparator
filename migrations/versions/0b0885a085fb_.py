"""empty message

Revision ID: 0b0885a085fb
Revises: 27c1671f61a7
Create Date: 2021-02-11 16:47:37.117863

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b0885a085fb'
down_revision = '27c1671f61a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contributor', sa.Column('admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contributor', 'admin')
    # ### end Alembic commands ###