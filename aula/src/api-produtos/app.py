from fastapi import FastAPI
from models.product import Product

app = FastAPI()

@app.get('/')
def say():
    return {'Fast': 'Hello'}

@app.get('/api/name/{name}') # endpoint
def say_hello(name:str):
    if not name:
        pass
    else:
        return {'Hello': name}

products = [
    Product(id=1, name='coca-cola', description='Refrigerante', price=9.98),
    Product(id=2, name='Tenis nike', description='Calçado', price=150.89),
    Product(id=3, name='Carro', description='Veiculo', price=9000.98),
]

@app.get('/api/products')
def get_products():
    return products

@app.get('/api/products/sale')
def get_sale():
    """
    Endpoitn que exibe o produco com maior desconto
    """
    return products[1]