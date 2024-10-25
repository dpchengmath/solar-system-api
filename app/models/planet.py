from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    diameter: Mapped[int]

# class Planet:
#     def __init__(self, id, name, description):
#         self.id = id
#         self.name = name
#         self.description = description

#     planets = [
#         Planet(1, "Neptune", "Giant and icy planet", 49244),
#         Planet(2, "Uranus", "Rotates on its side", 50724),
#         Planet(3, "Saturn", "Has beautiful rings", 116460),
#         Planet(4, "Jupiter", "Largest planet in the solar system", 139820),
#         Planet(5, "Mars", "The red planet", 6779),
#         Planet(6, "Earth", "Our home planet", 12742),
#         Planet(7, "Venus", "Second planet from the sun", 12104),
#         Planet(8, "Mercury", "Smallest and hottest planet", 4879),
#         Planet(6, "Pluto", "The planet they declassified as a planet", 2377)
#     ]