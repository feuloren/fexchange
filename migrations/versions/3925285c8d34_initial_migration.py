# -*- coding:utf-8 -*-

"""Initial migration

Revision ID: 3925285c8d34
Revises: None
Create Date: 2013-06-24 01:33:08.077509

"""

# revision identifiers, used by Alembic.
revision = '3925285c8d34'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(length=20), nullable=False),
    sa.Column('description', sa.String(length=140), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('utilisateurs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(length=10), nullable=True),
    sa.Column('prenom', sa.String(length=30), nullable=False),
    sa.Column('nom', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('mdp', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('offres',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vendeur_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('pret', 'don', 'vente', 'achat'), nullable=False),
    sa.Column('nom', sa.String(length=20), nullable=False),
    sa.Column('categorie_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('date_depart', sa.DateTime(), nullable=False),
    sa.Column('date_conclusion', sa.DateTime(), nullable=True),
    sa.Column('date_annule', sa.DateTime(), nullable=True),
    sa.Column('date_achat', sa.Date(), nullable=True),
    sa.Column('date_disponibilite', sa.Date(), nullable=False),
    sa.Column('etat', sa.Enum(u'neuf', u'comme neuf', u'bon', u'use', u'degrade'), nullable=False),
    sa.ForeignKeyConstraint(['categorie_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['vendeur_id'], ['utilisateurs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_retour', sa.Date(), nullable=True),
    sa.Column('duree', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['offres.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ventes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prix', sa.Numeric(precision=6, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['offres.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('offre_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('date_upload', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['offre_id'], ['offres.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    op.drop_table('photos')
    op.drop_table('ventes')
    op.drop_table('prets')
    op.drop_table('offres')
    op.drop_table('utilisateurs')
    op.drop_table('categories')
