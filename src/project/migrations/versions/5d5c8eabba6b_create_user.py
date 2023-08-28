"""create user.

Revision ID: 5d5c8eabba6b
Revises: 
Create Date: 2023-08-23 15:05:55.790976

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '5d5c8eabba6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False, comment='user`s name'),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_users')
    # ### end Alembic commands ###