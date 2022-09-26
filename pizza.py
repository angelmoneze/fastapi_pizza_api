from fastapi import APIRouter, Path, HTTPException, status
from model import Pizza, PizzaItem, PizzaItems

pizza_router = APIRouter()

pizza_list = []

#les endpoints

#enpoint pour ajouter pizza
@pizza_router.post("/pizza", status_code=201)
async def add_pizza(pizza: Pizza) -> dict:
    pizza_list.append(pizza)
    return { "message": "Pizza added successfully" }


#enpoint pour récupérer toutes les pizzas
@pizza_router.get("/pizza", response_model=PizzaItems)
async def retrieve_pizza() -> dict:
    return { "pizzas": pizza_list }


#enpoint pour récupérer une seule pizza
@pizza_router.get("/pizza/{pizza_id}")
async def get_single_pizza(pizza_id: int = Path(..., title="L'ID de la pizza à récupérer")) -> dict:
    for pizza in pizza_list:
        if pizza.id == pizza_id:
            return { "pizza" : pizza }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Pizza with supplied ID doesn't exists",
    )


#endpoint pour mettre à jour une pizza
@pizza_router.put("/pizza/{pizza_id}")
async def update_pizza(pizza_data: PizzaItem, pizza_id: int = Path(...,title="The ID of the pizza to be updated")) -> dict:
    for pizza in pizza_list:
        if pizza.id == pizza_id:
            pizza.item = pizza_data.item
            return {
                "message": "Pizza updated successfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Pizza with supplied ID doesn't exists",
    )

#endpoint pour supprimer une pizza
@pizza_router.delete("/pizza/{pizza_id}")
async def delete_single_pizza(pizza_id: int) -> dict:
    for index in range(len(pizza_list)):
        pizza = pizza_list[index]
        if pizza.id == pizza_id:
            pizza_list.pop(index)
            return{
                "message": "Pizza delated successfully"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Pizza with supplied ID doesn't exists"
    )

#endpoint pour supprimer toutes les pizzas
@pizza_router.delete("/pizza")
async def delete_all_pizza() -> dict:
    pizza_list.clear()
    return {
        "message": "Pizzas deleted Successfully"
    }