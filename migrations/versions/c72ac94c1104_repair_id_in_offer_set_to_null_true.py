"""repair id in offer set to null true

Revision ID: c72ac94c1104
Revises: d62876131029
Create Date: 2022-08-21 23:53:30.276294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c72ac94c1104'
down_revision = 'd62876131029'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('offer', 'repair_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('offer', 'repair_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
