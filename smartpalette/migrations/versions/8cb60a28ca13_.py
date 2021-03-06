"""empty message

Revision ID: 8cb60a28ca13
Revises: d71553f087ce
Create Date: 2018-12-04 19:51:43.433091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8cb60a28ca13'
down_revision = 'd71553f087ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('count', sa.Column('num', sa.Integer(), nullable=True, unique=False))
    op.drop_column('count', 'currentCount')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('count', sa.Column('currentCount', sa.INTEGER(), server_default=sa.text('nextval(\'"count_currentCount_seq"\'::regclass)'), autoincrement=True, nullable=False))
    op.drop_column('count', 'num')
    # ### end Alembic commands ###
