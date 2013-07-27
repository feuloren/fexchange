"""Duree en str

Revision ID: 177cfac90ef8
Revises: 338adf824248
Create Date: 2013-07-18 00:09:39.020132

"""

# revision identifiers, used by Alembic.
revision = '177cfac90ef8'
down_revision = '338adf824248'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_column('prets', 'duree')
    op.add_column('prets', sa.Column('duree', sa.String(20), nullable=True))

def downgrade():
    op.drop_column('prets', 'duree')
    op.add_column('prets', sa.Column('duree', sa.Integer), nullable=True)
