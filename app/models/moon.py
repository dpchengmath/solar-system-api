from sqlalchemy.orm import Mapped, mapped_column, relationship
from models import Planet
from ..db import db

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    planets: Mapped[list["Planet"]] = relationship(back_populates="moon")
