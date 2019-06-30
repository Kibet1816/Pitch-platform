"""Add password column

Revision ID: 50ef302ed395
Revises: 2bfc7a1fb88f
Create Date: 2019-06-30 15:10:35.183137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50ef302ed395'
down_revision = '2bfc7a1fb88f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    # ### end Alembic commands ###