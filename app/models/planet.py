from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    diameter: Mapped[int]
    moon_id: Mapped[Optional[int]] = mapped_column(ForeignKey("moon.id"))
    moon: Mapped[Optional["Moon"]] = relationship(back_populates="planets")

    
    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            diameter=self.diameter,
            moon=self.moon.name if moon else None
        )
    
    @classmethod
    def from_dict(cls, planet_data):
        new_planet = cls(
            title=planet_data["title"],
            description=planet_data["description"],
            diameter=planet_data["diameter"],
            moon_id=planet_data.get("moon_id", None)
        )

        return new_planet