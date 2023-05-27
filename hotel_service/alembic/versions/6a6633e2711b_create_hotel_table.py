"""Create hotel table

Revision ID: 6a6633e2711b
Revises: 
Create Date: 2023-05-27 00:01:05.523398

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from src.db.models.rental_space import STATUS_TYPES

# revision identifiers, used by Alembic.
revision = '6a6633e2711b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('country',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('currency',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('icon_image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('property_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('icon_image', sa.String(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('icon_image', sa.String(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('city',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('country_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['country_id'], ['country.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rental_space',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('bedroom_count', sa.Integer(), nullable=True),
    sa.Column('bathroom_count', sa.Integer(), nullable=True),
    sa.Column('property_type_id', sa.Integer(), nullable=False),
    sa.Column('room_type_id', sa.Integer(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('currency_id', sa.Integer(), nullable=False),
    sa.Column('status', sqlalchemy_utils.types.choice.ChoiceType(STATUS_TYPES), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['currency_id'], ['currency.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['property_type_id'], ['property_type.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['room_type_id'], ['room_type.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rental_space')
    op.drop_table('city')
    op.drop_table('room_type')
    op.drop_table('property_type')
    op.drop_table('currency')
    op.drop_table('country')
    op.drop_table('category')
    # ### end Alembic commands ###