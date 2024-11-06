import mysql.connector as db
from Utils.Credentials.CredUtils import Credentials

from tkinter import simpledialog, Tk
import sys

class Aeronet:
    def get_valid_connection(self) -> object:
        root = Tk()
        root.withdraw()
        
        root.protocol('WM_DELETE_WINDOW', lambda: sys.exit(0))
        
        password : str = Credentials.get_password()
        if not password:
            password = self.get_password_input(root)
            if password is None:
                root.destroy()
                sys.exit(0)

        while True:
            try:
                myDB = db.connect(
                    host="localhost", 
                    user="root", 
                    password=password
                )
                Credentials.set_password(password)
                root.destroy()
                return myDB
            except db.errors.ProgrammingError:
                password = self.get_password_input(root)
                if password is None:
                    root.destroy()
                    sys.exit(0)

    def get_password_input(self, root) -> str:
        while True:
            password = simpledialog.askstring(
                "MySQL Password", 
                "Please enter your my-sql password:", 
                show='*',
                parent=root
            )
            if password is None:
                return None
            if password.strip():
                return password

    def initialize_database(self, cursor : object) -> None:
        cursor.execute("CREATE DATABASE IF NOT EXISTS Aeronet")
        cursor.execute("USE Aeronet")

        tables = {
            "FlightPath": """
                CREATE TABLE IF NOT EXISTS FlightPath (
                    flight_no VARCHAR(8),
                    waypoint VARCHAR(200),
                    dist_from_wp DECIMAL(4, 2),
                    rate_assign VARCHAR(7)
                )
            """,
            "FM_Data": """
                CREATE TABLE IF NOT EXISTS FM_Data (
                    flight_no VARCHAR(15),
                    heading INT,
                    coordinates VARCHAR(90),
                    altitude INT,
                    air_speed INT,
                    climb_rate INT
                )
            """,
            "Schedule": """
                CREATE TABLE IF NOT EXISTS Schedule (
                    flight_no VARCHAR(8),
                    dep_time VARCHAR(25)
                )
            """,
            "Weather": """
                CREATE TABLE IF NOT EXISTS Weather (
                    description VARCHAR(18),
                    precipitation INT,
                    wind_speed INT,
                    cloud_base INT,
                    last_updated VARCHAR(25)
                )
            """
        }

        for query in tables.values():
            cursor.execute(query)

        for table in tables.keys():
            cursor.execute(f"DELETE FROM {table}")

        cursor.execute("""
            INSERT INTO Weather VALUE(
                "Sunny",
                10,
                0,
                6500,
                "2024-08-01 19:09:00"
            )
        """)

    def main(self) -> None:
        myDB = self.get_valid_connection()
        cursor = myDB.cursor()
        
        self.initialize_database(cursor)
        
        myDB.commit()
        
        from Interface.Interface import Interface
        Interface()

if __name__ == "__main__":
    Aeronet = Aeronet()
    Aeronet.main()
