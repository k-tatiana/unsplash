"""empty message

Revision ID: 6b70a7ed2a00
Revises: c38357be8437
Create Date: 2018-07-26 16:44:56.771302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b70a7ed2a00'
down_revision = 'c38357be8437'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_images_image_url', table_name='images')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_images_image_url', 'images', ['image_url'], unique=False)
    # ### end Alembic commands ###
