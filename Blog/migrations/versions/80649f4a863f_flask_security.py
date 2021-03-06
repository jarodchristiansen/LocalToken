"""flask-security

Revision ID: 80649f4a863f
Revises: 6d6dc76282eb
Create Date: 2020-07-17 16:35:16.508536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '80649f4a863f'
down_revision = '6d6dc76282eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('role', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True))
    # ### end Alembic commands ###
