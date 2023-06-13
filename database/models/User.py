from typing import Optional
from .Base import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import String, ForeignKey
from .Adress import Adress


class UserTable(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    adresses: Mapped[list["Adress"]] = relationship(
        back_populates="user", cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:  
        return f"User(id={self.id!r}, name={self.username!r}, fullname={self.fullname!r})"