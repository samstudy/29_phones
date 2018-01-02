"""Add a column for beautiful number

Revision ID: 779a1800922a
Revises:
Create Date: 2017-09-25 21:27:29.090345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '779a1800922a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('orders', sa.Column('upd_number', sa.Integer))
    pass


def downgrade():
    op.drop_column('orders', 'upd_number')
    pass
