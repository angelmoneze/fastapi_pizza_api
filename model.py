from doctest import Example
from msilib import schema
from pydantic import BaseModel
from typing import List

#creation des models pour la validation des requêtes

class Item(BaseModel):
    item: str
    status: str

class Pizza(BaseModel):
    id: int
    item: str
    pizzeria: str
    isbn: str

class PizzaItem(BaseModel):
    item : str

    class Config:
        schema_extra = {
            "example": {
                "item": "Buy the next pizza"
            }
        }

#ce modèle défini le format de la reponse pour récupérer toutes les pizzas
class PizzaItems(BaseModel):
    pizzas: List[PizzaItem]

    class Config:
        schema_extra = {
            "example": {
                "pizzas": [
                    {
                        "item": "Example schema 1 !"
                    },
                    {
                        "item": "Example schema 2 !"
                    }
                ]
            }
        }
