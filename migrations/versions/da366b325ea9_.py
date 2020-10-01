"""empty message

Revision ID: da366b325ea9
Revises: 095e452d38d8
Create Date: 2020-09-30 17:52:20.650136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da366b325ea9'
down_revision = '095e452d38d8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('slackUID', sa.String(), nullable=True))


def downgrade():
    op.drop_column('users', 'slackUID')
