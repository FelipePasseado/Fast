from product import Product
import json

def generate_products():
    f = (open('./data/products.json'))

    data = json.loads(f.read())
    f.close()
    return data















   #isso aqui foi pra criar um banco de dados de mentira for x in range(10):
   #     p = product(name = f'product{x+1}', price = 4.90 * x)
    #    list_products.append(p)

   # return list_products
    
