"""Messages et propositions

Revision ID: 338adf824248
Revises: 3925285c8d34
Create Date: 2013-07-11 00:22:31.640797

"""

# revision identifiers, used by Alembic.
revision = '338adf824248'
down_revision = '3925285c8d34'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('propositions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('pret', 'don', 'vente'), nullable=False),
    sa.Column('utilisateur', sa.Integer(), nullable=False),
    sa.Column('date_proposition', sa.DateTime(), nullable=False),
    sa.Column('date_accepte', sa.DateTime(), nullable=True),
    sa.Column('date_refuse', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['utilisateur'], ['utilisateurs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('de', sa.Integer(), nullable=False),
    sa.Column('pour', sa.Integer(), nullable=False),
    sa.Column('offre', sa.Integer(), nullable=True),
    sa.Column('proposition', sa.Integer(), nullable=True),
    sa.Column('contenu', sa.Text(), nullable=False),
    sa.Column('date_envoi', sa.DateTime(), nullable=False),
    sa.Column('date_lecture', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['de'], ['utilisateurs.id'], ),
    sa.ForeignKeyConstraint(['offre'], ['offres.id'], ),
    sa.ForeignKeyConstraint(['pour'], ['utilisateurs.id'], ),
    sa.ForeignKeyConstraint(['proposition'], ['propositions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pprets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_retour', sa.Date(), nullable=True),
    sa.Column('duree', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['propositions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('achats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prix', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['propositions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('achats')
    op.drop_table('pprets')
    op.drop_table('messages')
    op.drop_table('propositions')
