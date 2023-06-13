from .Base import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import String, ForeignKey
from .User import UserTable

class Adress(Base):
    __tablename__ = "adress"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["UserTable"] = relationship(back_populates="adresses")