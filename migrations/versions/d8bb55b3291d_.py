"""empty message

Revision ID: d8bb55b3291d
Revises: 1fed124866bf
Create Date: 2023-10-02 21:54:00.126399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8bb55b3291d'
down_revision = '1fed124866bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_crypto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('crypto_id', sa.Integer(), nullable=False),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['crypto_id'], ['crypto.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('crypto', schema=None) as batch_op:
        batch_op.drop_column('notes')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('crypto', schema=None) as batch_op:
        batch_op.add_column(sa.Column('notes', sa.TEXT(), autoincrement=False, nullable=True))

    op.drop_table('user_crypto')
    # ### end Alembic commands ###
