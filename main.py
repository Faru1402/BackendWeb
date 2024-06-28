from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.service import products

app = FastAPI(title= 'Tarea 8',
    description='Esta es la tarea 8', 
    version='1.0')

# Solucion CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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