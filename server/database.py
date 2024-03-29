import time
import sqlite3
import json

class DataBase:
    def __init__(self, db_file='metingen.db'):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
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

    def get_readings(self, aantal,sensor_id):
        readings = []

        query = f'SELECT * FROM sensor_data WHERE sensor_id == ? ORDER BY id DESC LIMIT ?'
        with self.conn:
            cursor = self.conn.execute(query, (sensor_id, aantal))
            r = cursor.fetchall()
            for reading in r:
                x = {
                    "sensor_id": reading[1],
                    "temperatuur": reading[2],
                    "lucht_vochtigheid": reading[3],
                    "lucht_druk": reading[4],
                    "gas": reading[5],
                    "x": reading[6],
                    "y": reading[7],
                    "tijd": reading[8]
                }
                readings.append(x)

        return json.dumps(readings)
    
    def clear(self):
        query = '''delete from sensor_data'''
        
        with self.conn:
            self.conn.execute(query)        
            
    def close_connection(self):
        self.conn.close()
        
