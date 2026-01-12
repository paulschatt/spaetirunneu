"""init

Revision ID: 6fb1680a7f9a
Revises: 
Create Date: 2026-01-12 14:10:52.019007

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6fb1680a7f9a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # pgcrypto extension
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")

    # spaetirun
    op.create_table(
        "spaetirun",
        sa.Column("id", sa.UUID, primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("name", sa.Text),
        sa.Column("created_at", sa.TIMESTAMP, nullable=False,
                  server_default=sa.text("transaction_timestamp()")),
    )

    # challenge
    op.create_table(
        "challenge",
        sa.Column("id", sa.UUID, primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("name", sa.Text),
        sa.Column("description", sa.Text),
        sa.Column("points", sa.Integer, nullable=False),
        sa.Column("max_times", sa.Integer),
        sa.Column("spaetirun_id", sa.UUID, sa.ForeignKey("spaetirun.id")),
        sa.Column("created_at", sa.TIMESTAMP, nullable=False,
                  server_default=sa.text("transaction_timestamp()")),
    )

    # team
    op.create_table(
        "team",
        sa.Column("id", sa.UUID, primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("name", sa.Text),
        sa.Column("spaetirun_id", sa.UUID, sa.ForeignKey("spaetirun.id")),
        sa.Column("created_at", sa.TIMESTAMP, nullable=False,
                  server_default=sa.text("transaction_timestamp()")),
    )

    # player
    op.create_table(
        "player",
        sa.Column("id", sa.UUID, primary_key=True, server_default=sa.text("gen_random_uuid()")),
        sa.Column("name", sa.Text),
        sa.Column("team_id", sa.UUID, sa.ForeignKey("team.id")),
        sa.Column("spaetirun_id", sa.UUID, sa.ForeignKey("spaetirun.id")),
        sa.Column("created_at", sa.TIMESTAMP, nullable=False,
                  server_default=sa.text("transaction_timestamp()")),
    )


def downgrade():
    op.drop_table("player")
    op.drop_table("team")
    op.drop_table("challenge")
    op.drop_table("spaetirun")
    op.execute("DROP EXTENSION IF EXISTS pgcrypto")