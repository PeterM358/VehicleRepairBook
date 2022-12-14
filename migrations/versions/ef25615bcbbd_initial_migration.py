"""Initial migration

Revision ID: ef25615bcbbd
Revises: 
Create Date: 2022-08-07 18:36:20.969120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef25615bcbbd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Enum('mechanic', 'vehicle_owner', 'admin', name='userrole'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('mechanic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Enum('mechanic', 'vehicle_owner', 'admin', name='userrole'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehicle_owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Enum('mechanic', 'vehicle_owner', 'admin', name='userrole'), nullable=False),
    sa.Column('mechanics', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mechanics'], ['mechanic.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vehicle_type', sa.Enum('car', 'truck', 'motorcycle', name='vehicletype'), nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('year_of_registration', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('vehicle_owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['vehicle_owner_id'], ['vehicle_owner.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('repair',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('photo_url', sa.String(length=255), nullable=False),
    sa.Column('vehicle_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('repair')
    op.drop_table('vehicle')
    op.drop_table('vehicle_owner')
    op.drop_table('mechanic')
    op.drop_table('admin')
    # ### end Alembic commands ###
