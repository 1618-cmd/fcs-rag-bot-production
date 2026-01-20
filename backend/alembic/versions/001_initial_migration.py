"""Initial migration: create users, query_logs, and tenants tables

Revision ID: 001_initial
Revises: 
Create Date: 2026-01-20 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create tenants table
    op.create_table(
        'tenants',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=True, server_default='true'),
        sa.Column('max_users', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create users table
    op.create_table(
        'users',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('tenant_id', sa.String(), nullable=False),
        sa.Column('password_hash', sa.String(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=True, server_default='true'),
        sa.Column('full_name', sa.String(), nullable=True),
        sa.Column('role', sa.String(), nullable=False, server_default='viewer'),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('last_login', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_index('idx_tenant_email', 'users', ['tenant_id', 'email'], unique=False)
    op.create_index('idx_tenant_role', 'users', ['tenant_id', 'role'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=False)
    op.create_index(op.f('ix_users_tenant_id'), 'users', ['tenant_id'], unique=False)
    
    # Create query_logs table
    op.create_table(
        'query_logs',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('tenant_id', sa.String(), nullable=False),
        sa.Column('user_id', sa.String(), nullable=True),
        sa.Column('user_email', sa.String(), nullable=True),
        sa.Column('question', sa.Text(), nullable=False),
        sa.Column('answer_preview', sa.Text(), nullable=True),
        sa.Column('answer_full', sa.Text(), nullable=True),
        sa.Column('sources_count', sa.Integer(), nullable=True, server_default='0'),
        sa.Column('sources_list', postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column('latency_ms', sa.Float(), nullable=False),
        sa.Column('was_cached', sa.Boolean(), nullable=True, server_default='false'),
        sa.Column('was_refusal', sa.Boolean(), nullable=True, server_default='false'),
        sa.Column('refusal_reason', sa.Text(), nullable=True),
        sa.Column('feedback', sa.String(), nullable=True),
        sa.Column('feedback_timestamp', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_tenant_user', 'query_logs', ['tenant_id', 'user_id'], unique=False)
    op.create_index('idx_tenant_created', 'query_logs', ['tenant_id', 'created_at'], unique=False)
    op.create_index('idx_user_created', 'query_logs', ['user_id', 'created_at'], unique=False)
    op.create_index(op.f('ix_query_logs_id'), 'query_logs', ['id'], unique=False)
    op.create_index(op.f('ix_query_logs_tenant_id'), 'query_logs', ['tenant_id'], unique=False)
    op.create_index(op.f('ix_query_logs_user_id'), 'query_logs', ['user_id'], unique=False)
    op.create_index(op.f('ix_query_logs_user_email'), 'query_logs', ['user_email'], unique=False)
    op.create_index(op.f('ix_query_logs_created_at'), 'query_logs', ['created_at'], unique=False)


def downgrade() -> None:
    # Drop tables in reverse order
    op.drop_index(op.f('ix_query_logs_created_at'), table_name='query_logs')
    op.drop_index(op.f('ix_query_logs_user_email'), table_name='query_logs')
    op.drop_index(op.f('ix_query_logs_user_id'), table_name='query_logs')
    op.drop_index(op.f('ix_query_logs_tenant_id'), table_name='query_logs')
    op.drop_index(op.f('ix_query_logs_id'), table_name='query_logs')
    op.drop_index('idx_user_created', table_name='query_logs')
    op.drop_index('idx_tenant_created', table_name='query_logs')
    op.drop_index('idx_tenant_user', table_name='query_logs')
    op.drop_table('query_logs')
    
    op.drop_index(op.f('ix_users_tenant_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index('idx_tenant_role', table_name='users')
    op.drop_index('idx_tenant_email', table_name='users')
    op.drop_table('users')
    
    op.drop_table('tenants')
