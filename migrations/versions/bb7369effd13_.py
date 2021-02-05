"""empty message

Revision ID: bb7369effd13
Revises: 
Create Date: 2021-01-21 15:38:59.189319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb7369effd13'
down_revision = None
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