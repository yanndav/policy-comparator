"""empty message

Revision ID: 27c1671f61a7
Revises: 
Create Date: 2021-02-11 16:32:28.088069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27c1671f61a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('article',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation', sa.Date(), nullable=False),
    sa.Column('update', sa.Date(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('journal', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('link'),
    sa.UniqueConstraint('title')
    )
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation', sa.Date(), nullable=False),
    sa.Column('update', sa.Date(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contributor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('sheet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation', sa.Date(), nullable=False),
    sa.Column('update', sa.Date(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('abstract', sa.Text(), nullable=False),
    sa.Column('policy', sa.String(), nullable=False),
    sa.Column('target', sa.String(), nullable=False),
    sa.Column('submit', sa.Boolean(), nullable=False),
    sa.Column('publish', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('articleAuthor',
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], )
    )
    op.create_table('contributorArticle',
    sa.Column('contributor_id', sa.Integer(), nullable=True),
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['contributor_id'], ['contributor.id'], )
    )
    op.create_table('contributorSheet',
    sa.Column('contributor_id', sa.Integer(), nullable=True),
    sa.Column('sheet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contributor_id'], ['contributor.id'], ),
    sa.ForeignKeyConstraint(['sheet_id'], ['sheet.id'], )
    )
    op.create_table('result',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation', sa.Date(), nullable=False),
    sa.Column('update', sa.Date(), nullable=False),
    sa.Column('sheet_id', sa.Integer(), nullable=True),
    sa.Column('article_id', sa.Integer(), nullable=True),
    sa.Column('policy', sa.String(), nullable=False),
    sa.Column('target', sa.String(), nullable=False),
    sa.Column('policyUnit', sa.String(), nullable=True),
    sa.Column('targetUnit', sa.String(), nullable=True),
    sa.Column('method', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('yearPolicy', sa.Integer(), nullable=False),
    sa.Column('estimate', sa.Float(), nullable=False),
    sa.Column('standardError', sa.Float(), nullable=False),
    sa.Column('sampleSize', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['sheet_id'], ['sheet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contributorResult',
    sa.Column('contributor_id', sa.Integer(), nullable=True),
    sa.Column('result_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['contributor_id'], ['contributor.id'], ),
    sa.ForeignKeyConstraint(['result_id'], ['result.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contributorResult')
    op.drop_table('result')
    op.drop_table('contributorSheet')
    op.drop_table('contributorArticle')
    op.drop_table('articleAuthor')
    op.drop_table('sheet')
    op.drop_table('contributor')
    op.drop_table('author')
    op.drop_table('article')
    # ### end Alembic commands ###