from fastapi import FastAPI
from app.service import products
app = FastAPI()


@app.get("/")
def read_root():
    return {"backend": "0.01"}

@app.get("/get_product_specification/{product_name}")
def get_product_specification(product_name: str):
    """function to get product specification"""
    product = products.products()
    result = product.get_products(product_name)
    
    return{"result": result}