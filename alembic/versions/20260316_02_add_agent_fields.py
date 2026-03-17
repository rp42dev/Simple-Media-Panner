"""Add agent output fields to content_items table"""
# Alembic revision identifiers
revision = '20260316_02_add_agent_fields'
down_revision = '20260316_01_create_content_items'
branch_labels = None
depends_on = None
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.add_column('content_items', sa.Column('seo', sa.Text))
    op.add_column('content_items', sa.Column('analytics', sa.Text))
    op.add_column('content_items', sa.Column('video', sa.Text))
    op.add_column('content_items', sa.Column('carousel', sa.Text))

def downgrade():
    op.drop_column('content_items', 'seo')
    op.drop_column('content_items', 'analytics')
    op.drop_column('content_items', 'video')
    op.drop_column('content_items', 'carousel')
