import json


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