"""Utilisateur contraintes Unique

Revision ID: 3819806e8fa8
Revises: 177cfac90ef8
Create Date: 2014-01-16 19:36:13.450718

"""

# revision identifiers, used by Alembic.
revision = '3819806e8fa8'
down_revision = '177cfac90ef8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_unique_constraint(None, 'utilisateurs', ['login',])
    op.create_unique_constraint(None, 'utilisateurs', ['email',])

def downgrade():
    op.drop_constraint('email', 'utilisateurs', 'unique')
    op.drop_constraint('login', 'utilisateurs', 'unique')
