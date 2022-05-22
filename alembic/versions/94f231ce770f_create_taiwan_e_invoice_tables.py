"""Create Taiwan e-invoice tables

Revision ID: 94f231ce770f
Revises: 
Create Date: 2022-05-23 02:16:26.121475

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "94f231ce770f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "invoice",
        sa.Column("number", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("card_type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("card_number", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("seller_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("status", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("donatable", sa.Boolean(), nullable=False),
        sa.Column("amount", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("period", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("donate_mark", sa.Integer(), nullable=False),
        sa.Column("seller_tax_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("seller_address", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("buyer_tax_id", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("currency", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("timestamp", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("number"),
    )
    op.create_table(
        "invoice_carrier",
        sa.Column("id", sa.Integer(), nullable=True),
        sa.Column("type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("card_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "invoice_detail",
        sa.Column("id", sa.Integer(), nullable=True),
        sa.Column("row_number", sa.Integer(), nullable=False),
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("quantity", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("unit_price", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("amount", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("invoice_number", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.ForeignKeyConstraint(
            ["invoice_number"],
            ["invoice.number"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("invoice_detail")
    op.drop_table("invoice_carrier")
    op.drop_table("invoice")
    # ### end Alembic commands ###
