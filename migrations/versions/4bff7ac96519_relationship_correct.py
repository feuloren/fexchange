"""Relationship correctes

Revision ID: 4bff7ac96519
Revises: 3819806e8fa8
Create Date: 2014-01-17 14:08:10.937052

"""

# revision identifiers, used by Alembic.
revision = '4bff7ac96519'
down_revision = '3819806e8fa8'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def change_column_name_with_fk(table, col_name, new_name, fk, fk_referent, fk_cols):
    op.drop_constraint(fk, table, type_='foreignkey')
    op.alter_column(table, col_name, new_column_name=new_name, existing_type=sa.Integer, existing_server_default=0, existing_nullable=False)
    op.create_foreign_key(fk, table, fk_referent, [new_name], [fk_cols])

updates = (['messages', 'de', 'emetteur_id', 'messages_ibfk_1', 'utilisateurs', 'id'],
           ['messages', 'pour', 'destinataire_id', 'messages_ibfk_3', 'utilisateurs', 'id'],
           ['messages', 'offre', 'offre_id', 'messages_ibfk_2', 'offres', 'id'],
           ['propositions', 'utilisateur', 'utilisateur_id', 'propositions_ibfk_1', 'utilisateurs', 'id']
           )

def upgrade():
    for i in updates:
        change_column_name_with_fk(*i)

def downgrade():
    for i in updates:
        i[1], i[2] = i[2], i[1]
        change_column_name_with_fk(*i)
