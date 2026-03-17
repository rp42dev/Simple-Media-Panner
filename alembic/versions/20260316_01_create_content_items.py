"""Initial migration: create content_items table"""
# Alembic revision identifiers
revision = '20260316_01_create_content_items'
down_revision = None
branch_labels = None
depends_on = None
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'content_items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('topic', sa.String(255)),
        sa.Column('category', sa.String(100)),
        sa.Column('tone', sa.String(100)),
        sa.Column('content', sa.Text),
        sa.Column('visuals', sa.Text),
    )

def downgrade():
    op.drop_table('content_items')
