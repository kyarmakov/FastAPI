from passlib.context import CryptContext
from sqlmodel import SQLModel, Field, Relationship, Column, VARCHAR


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


class TripInput(SQLModel):
    start: int
    end: int
    description: str


class TripOutput(TripInput):
    id: int


class Trip(TripInput, table=True):
    id: int | None = Field(primary_key=True, default=None)
    car_id: int = Field(foreign_key='car.id')
    car: "Car" = Relationship(back_populates='trips')


class CarInput(SQLModel):
    size: str
    fuel: str | None = 'electric'
    doors: int
    transmission: str | None = 'auto'


class Car(CarInput, table=True):
    id: int | None = Field(primary_key=True, default=None)
    trips: list[Trip] = Relationship(back_populates='car')


class CarOutput(CarInput):
    id: int
    trips: list[TripOutput] = []


class UserOutput(SQLModel):
    id: int
    username: str


class User(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    username: str = Field(sa_column=Column('username', VARCHAR, unique=True, index=True))
    password_hash: str = ''

    def set_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
