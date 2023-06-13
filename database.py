from typing import List, Optional
from sqlalchemy import (Column, ForeignKey, Integer, MetaData, String, Table,
                        create_engine, text)
from sqlalchemy.orm import (Mapped, DeclarativeBase, mapped_column,
                            relationship)
from sqlalchemy import insert, select
from sqlalchemy.orm import Session  
import config


engine = create_engine(
    url=config.SQLALCHEMY_URL, 
    echo=config.SQLACLHEMY_ECHO
)


class Base(DeclarativeBase):
    pass


class UserTable(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    fullname: Mapped[Optional[str]]

    adresses: Mapped[list["Adress"]] = relationship(
        back_populates="user", cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:  
        return f"User(id={self.id!r}, name={self.username!r}, fullname={self.fullname!r})"
    

class Adress(Base):
    __tablename__ = "adress"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["UserTable"] = relationship(back_populates="adresses")


def create_user(
        session: Session, 
        username: str, 
        fullname: str, 
        adresses: Optional[list["Adress"]] = None
        ):
    if adresses:
        session.add(UserTable(username=username, fullname=fullname, adresses=adresses))
    else:
        session.add(UserTable(username=username, fullname=fullname))
    session.commit()


def fetch_user(session: Session, username: str) -> UserTable | None:
    stmt = select(UserTable).where(UserTable.username == username)
    user: UserTable | None = session.scalar(stmt)
    return user


def add_adresses(session: Session, user: UserTable, *emails: str) -> None:
    user.adresses = [
        Adress(email=email)
        for email in emails
    ]
    session.commit()


   
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    with Session(engine) as session:

        # create_user(
        #     session=session,
        #     username="mrwhite",
        #     fullname="Walter White",
        #     adresses = [
        #         Adress(
        #             email="bitchlasagna@gmail.com",
        #         ),
        #         Adress(
        #             email="idometh@cia.com",
        #         ),
        #     ]
        # )

        # create_user(
        #     session=session,
        #     username="jesse ( . )  ( . )",
        #     fullname="Jesse Pinkman",
        #     adresses = [
        #         Adress(
        #             email="yoyoyo@gmail.com",
        #         ),
        #     ]
        # )
        print(fetch_user(session=session, username="adad"))