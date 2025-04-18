"""Add user relationship to Reservation

Revision ID: 542aa5f86b6c
Revises: ac671b91403e
Create Date: 2025-04-17 15:05:07.407260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '542aa5f86b6c'
down_revision = 'ac671b91403e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_reservation_user_id_user', 'user',
                                    ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.drop_constraint('fk_reservation_user_id_user',
                                 type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
