"""Initial Migration

Revision ID: ab67ea40134e
Revises: 
Create Date: 2020-11-03 16:20:25.216470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab67ea40134e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('courses')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('courses',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('full_time', sa.BOOLEAN(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###
