from pydantic import BaseModel

class Product(BaseModel): #isso aqui cria uma classe e atributo de maneira fácil
    name: str
    price: float
    