from app.dao import mysql


class products:
    def __init__(self):

        self.connection = mysql.Mysql(
            host="localhost",
            user="root",
            passwd="root",
        ).connect()

        self.connection.execute("USE inventario;")
        

    def get_products(self, name: str):
        """function to get products"""
        query = f"SELECT id, name, description, owner_id, justification FROM items WHERE name = '{name}'"
        self.connection.execute(query)
        result = self.connection.fetchall()
        json_result = {}
        for row in result:
            json_result = {
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'owner_id': row[3],
            'justification': row[4]
            }
        return json_result