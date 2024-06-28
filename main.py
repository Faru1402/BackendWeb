from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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


class products:
    def __init__(self):
        pass

    def get_products(self):
        """function to get products"""
        info = {
        "MANICURE": {
        "Acrilicas": "$150,000",
        "Polygel": "$125,000",
        "Press On": "$110,000",
        "Semipermanente": "$40,000",
        "Tradicional": "$20,000"
        },
        "PEDICURE": {
        "Semipermanente": "$50,000",
        "Tradicional": "$30,000"
        }
        }

        return info

    def get_service_price(self,category, subcategory):
        info = {
        "MANICURE": {
        "Acrilicas": "$150,000",
        "Polygel": "$125,000",
        "Press On": "$110,000",
        "Semipermanente": "$40,000",
        "Tradicional": "$20,000"
        },
        "PEDICURE": {
        "Semipermanente": "$50,000",
        "Tradicional": "$30,000"
        }
        }

        if category in info and subcategory in info[category]:
            return info[category][subcategory]
        else:
            return "Combination not found"