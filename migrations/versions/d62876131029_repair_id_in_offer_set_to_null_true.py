"""repair id in offer set to null true

Revision ID: d62876131029
Revises: 14a1b97b8f0f
Create Date: 2022-08-21 23:46:04.868928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd62876131029'
down_revision = '14a1b97b8f0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('offer_repair_id_fkey', 'offer', type_='foreignkey')
    op.create_foreign_key(None, 'offer', 'repair', ['repair_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'offer', type_='foreignkey')
    op.create_foreign_key('offer_repair_id_fkey', 'offer', 'repair', ['repair_id'], ['id'])
    # ### end Alembic commands ###
