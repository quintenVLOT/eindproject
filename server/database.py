import time
import sqlite3
import json

class DataBase:
    def __init__(self, db_file='metingen.db'):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.create_meetingen_table()
        self.create_kalibreer_table()

    def create_meetingen_table(self):
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
            
    def create_kalibreer_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS kalibratie_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sensor_id TEXT,
                temperatuur REAL
                lucht_vochtigheid REAL,
                lucht_druk REAL,
                gas REAL
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

    def insert_kalibratie(self, json):
        sensor_id = json['sensor_id']
        temperatuur = json['temperatuur']
        sensor_id = json['sensor_id']
        lucht_vochtigheid = json['luchtvochtigheid']
        lucht_druk = json['luchtdruk']
        
        # Controleren of een item met hetzelfde sensor_id al in de database staat
        existing_query = '''
            SELECT COUNT(*) FROM kalibratie_data WHERE sensor_id = ?
        '''
        with self.conn:
            existing_count = self.conn.execute(existing_query, (sensor_id,)).fetchone()[0]
            if existing_count > 0:
                # Overschrijven van de waarde als het item al bestaat
                update_query = '''
                    UPDATE kalibratie_data SET waarde = ? WHERE sensor_id = ?
                '''
                self.conn.execute(update_query, (waarde, sensor_id))
            else:
                # Toevoegen van een nieuw item als het item niet bestaat
                insert_query = '''
                    INSERT INTO kalibratie_data (sensor_id, waarde) VALUES (?, ?)
                '''
                self.conn.execute(insert_query, (sensor_id, waarde))

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

    def get_kalibratie(self, sensor_id):
        query = '''
            SELECT * FROM kalibratie_data WHERE sensor_id = ?
        '''
        with self.conn:
            result = self.conn.execute(query, (sensor_id)).fetchone()
            if result:
                # Gegevens gevonden voor de sensor_id
                x = {
                    "sensor_id": reading[1],
                    "temperatuur": reading[2],
                    "lucht_vochtigheid": reading[3],
                    "lucht_druk": reading[4],
                    "gas": reading[5],
                }
                return json.dumps(x)
            else:
                # Geen gegevens gevonden voor de sensor_id
                x = {
                    "sensor_id": sensor_id,
                    "temperatuur": 0,
                    "lucht_vochtigheid": 0,
                    "lucht_druk": 0,
                    "gas": 0,
                }
                return json.dumps(x)
    
    def clear_meetingen(self):
        query = '''delete from sensor_data'''
        
        with self.conn:
            self.conn.execute(query)
            
    def clear_kalibratie(self):
        query = '''delete from kalibratie_data'''
        
        with self.conn:
            self.conn.execute(query)      
            
    def close_connection(self):
        self.conn.close()
        
