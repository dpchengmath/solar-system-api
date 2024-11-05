from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    diameter: Mapped[int]
    explorer_id: Mapped[Optional[int]] = mapped_column(ForeignKey("explorer.id"))
    explorer: Mapped[list["Explorer"]] = relationship(back_populates="explorer")



    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["diameter"] = self.diameter
        

        return planet_as_dict
    
    @classmethod
    def from_dict(cls, planet_data):
        new_planet = cls(title=planet_data["title"],
                       description=planet_data["description"])

        return new_planet

# class Planet:
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description

#     planets = [
#         Planet(1, "Mercury", "Hottest planet", 4879),
#         Planet(2, "Venus", "Second planet from the sun", 12104),
#         Planet(3, "Earth", "Our home planet", 12742),
#         Planet(4, "Mars", "The red planet", 6779),
#         Planet(5, "Jupiter", "Largest planet in the solar system", 139820),
#         Planet(6, "Saturn", "Has beautiful rings", 116460),
#         Planet(7, "Uranus", "Rotates on its side", 50724),
#         Planet(8, "Neptune", "Giant and icy planet", 49244),
#         Planet(9, "Pluto", "The planet they declassified as a planet", 2377)
#     ]