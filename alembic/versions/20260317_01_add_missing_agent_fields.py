"""Add missing agent output fields to content_items table"""
from alembic import op
import sqlalchemy as sa

# Alembic revision identifiers
revision = '20260317_01_add_missing_agent_fields'
down_revision = '20260316_02_add_agent_fields'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('content_items', sa.Column('formatted_content', sa.Text))
    op.add_column('content_items', sa.Column('research_points', sa.Text))
    op.add_column('content_items', sa.Column('strategy', sa.Text))
    op.add_column('content_items', sa.Column('topics', sa.Text))
    op.add_column('content_items', sa.Column('visual_prompts', sa.Text))
    op.add_column('content_items', sa.Column('writer_output', sa.Text))

def downgrade():
    op.drop_column('content_items', 'formatted_content')
    op.drop_column('content_items', 'research_points')
    op.drop_column('content_items', 'strategy')
    op.drop_column('content_items', 'topics')
    op.drop_column('content_items', 'visual_prompts')
    op.drop_column('content_items', 'writer_output')
