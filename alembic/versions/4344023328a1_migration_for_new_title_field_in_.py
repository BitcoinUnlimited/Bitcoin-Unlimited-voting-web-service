"""Migration for new title field in proposal_metadata

Revision ID: 4344023328a1
Revises: bcd18782dfa0
Create Date: 2017-10-11 19:11:56.783136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4344023328a1'
down_revision = 'bcd18782dfa0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proposal_metadata', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('proposal_metadata', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###