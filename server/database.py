import time
import sqlite3
import json

class DataBase:
    def __init__(self, db_file='metingen.db'):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS sensor_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sensor_id TEXT,
                temperatuur REAL,
                lucht_vochtigheid REAL,
                lucht_druk REAL,
                gas REAL,
                x REAL,
                y REAL,
                tijd INTEGER
            )
        '''
        with self.conn:
            self.conn.execute(query)

    def insert_reading(self, json):
        gas = json['gas']
        temperatuur = json['temperatuur']
        sensor_id = json['sensor_id']
        lucht_vochtigheid = json['luchtvochtigheid']
        lucht_druk = json['luchtdruk']
        x = json['x']
        y = json['y']
        tijd = json['tijd']
        
        query = '''
            INSERT INTO sensor_data (sensor_id, temperatuur, lucht_vochtigheid, lucht_druk, gas, x, y, tijd)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        with self.conn:
            self.conn.execute(query, (sensor_id, temperatuur, lucht_vochtigheid, lucht_druk, gas, x, y, tijd))

    def get_all_readings(self):
        readings = []
        
        query = 'SELECT * FROM sensor_data'
        with self.conn:
            cursor = self.conn.execute(query)
            r = cursor.fetchall()
            for reading in r:
                x = {"id": reading[1], "temperatuur": reading[2], "lucht_vochtigheid": reading[3], "lucht_druk": reading[4], "gas": reading[5], "x": reading[6], "y": reading[7], "tijd": reading[8]}
                readings.append(json.dumps(x))
        
        return readings
            
    def close_connection(self):
        self.conn.close()
        
