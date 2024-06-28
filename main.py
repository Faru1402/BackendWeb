from fastapi import FastAPI
from app.service import products
app = FastAPI()


@app.get("/")
def read_root():
    return {"backend": "0.01"}

@app.get("/get_product_specification/")
def get_product_specification():
    """function to get product specification"""
    product = products.products()
    result = product.get_products()
    
    return{"result": result}

@app.get("/get_service_price/{category}/{subcategory}")
def get_service_price(category: str, subcategory: str):
    """function to get service price"""
    product = products.products()
    result = product.get_service_price(category, subcategory)
    return {"result": result}