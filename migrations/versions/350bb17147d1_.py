"""empty message

Revision ID: 350bb17147d1
Revises: 2b014857fbe9
Create Date: 2021-01-21 16:21:34.493321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '350bb17147d1'
down_revision = '2b014857fbe9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('result', sa.Column('policyUnit', sa.String(), nullable=False))
    op.add_column('result', sa.Column('targetUnit', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('result', 'targetUnit')
    op.drop_column('result', 'policyUnit')
    # ### end Alembic commands ###