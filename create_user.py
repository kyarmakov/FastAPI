from getpass import getpass

from sqlmodel import SQLModel, Session, create_engine

from schemas import User


engine = create_engine(
    "sqlite:///carsharing.db",
    connect_args={"check_same_thread": False},
    echo=True
)


if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)

    username = input("Please enter username\n")
    pwd = getpass("Please enter password\n")

    with Session(engine) as session:
        user = User(username=username)
        user.set_password(pwd)
        session.add(user)
        session.commit()
