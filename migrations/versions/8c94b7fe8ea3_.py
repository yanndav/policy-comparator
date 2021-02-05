"""empty message

Revision ID: 8c94b7fe8ea3
Revises: d524d5241597
Create Date: 2021-01-21 16:28:18.946483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8c94b7fe8ea3'
down_revision = 'd524d5241597'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('result', 'policyUnit',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('result', 'targetUnit',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('result', 'targetUnit',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('result', 'policyUnit',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###