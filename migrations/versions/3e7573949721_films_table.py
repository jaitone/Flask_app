"""films table

Revision ID: 3e7573949721
Revises: d6a6705c0e19
Create Date: 2021-03-23 11:23:10.602833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e7573949721'
down_revision = 'd6a6705c0e19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('films', 'rating')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('films', sa.Column('rating', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
