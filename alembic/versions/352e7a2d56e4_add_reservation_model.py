"""Add Reservation model

Revision ID: 352e7a2d56e4
Revises: cddb9c4d1710
Create Date: 2025-04-16 13:42:49.815261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '352e7a2d56e4'
down_revision = 'cddb9c4d1710'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_reserve', sa.DateTime(), nullable=True),
    sa.Column('to_reserve', sa.DateTime(), nullable=True),
    sa.Column('meetingroom_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['meetingroom_id'], ['meetingroom.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservation')
    # ### end Alembic commands ###
