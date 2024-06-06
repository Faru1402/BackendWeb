import pymysql
from fastapi import HTTPException

class Mysql:
    def __init__(self, host: str, user: str, passwd: str):
        self.host = host
        self.user = user
        self.passwd = passwd


    def connect(self):
        """function to create coneccion with db Mysql"""

        try:
            connection = pymysql.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                port=3306,
            )
            cursor = connection.cursor()
            return cursor

        except pymysql.err.OperationalError as e:
            raise HTTPException(status_code=404, detail=f"{e}") from e
        