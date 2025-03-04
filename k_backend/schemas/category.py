from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class CategoryBase(SQLModel):
    name: str
    description: str


class Category(CategoryBase, table=True):
    __tablename__ = "category"
    id: Optional[int] = Field(primary_key=True, nullable=False)
    entries: List["PaymentEntry"] = Relationship(back_populates="category")


class CategoryCreate(CategoryBase):
    pass


class CategoryRead(CategoryBase):
    id: int


from .payment import PaymentEntry
