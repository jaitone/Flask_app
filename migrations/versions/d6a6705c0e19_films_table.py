"""films table

Revision ID: d6a6705c0e19
Revises: 
Create Date: 2021-03-23 11:21:22.262295

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6a6705c0e19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('films',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('film_name', sa.String(length=128), nullable=False),
    sa.Column('img_url', sa.Text(), nullable=False),
    sa.Column('release_year', sa.Integer(), nullable=True),
    sa.Column('summary', sa.String(length=255), nullable=True),
    sa.Column('director', sa.String(length=128), nullable=True),
    sa.Column('genre', sa.String(length=128), nullable=True),
    sa.Column('rating', sa.String(length=128), nullable=True),
    sa.Column('film_runtime', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('films')
    # ### end Alembic commands ###
