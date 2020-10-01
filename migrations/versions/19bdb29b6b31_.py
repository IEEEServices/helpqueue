"""empty message

Revision ID: 19bdb29b6b31
Revises: da366b325ea9
Create Date: 2020-09-30 18:14:38.190702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19bdb29b6b31'
down_revision = 'da366b325ea9'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('tickets', sa.Column('mentor_slackUID', sa.String(), nullable=True))


def downgrade():
    op.drop_column('tickets', 'mentor_slackUID')