#!/home/sudharsan/myenv/bin/python3
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
db_name = os.getenv('DB_NAME')
pass_key = os.getenv('DB_PASSWORD')

def get_db_connection():
    """Get a new database connection."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=pass_key,
        database=db_name
    )

def check(mac):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM registered_mac WHERE mac_id=%s"
        cursor.execute(query, (mac,))
        result = cursor.fetchone()
        return result is not None
    finally:
        cursor.close()
        connection.close()

def update(mac, new_mac):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = "UPDATE registered_mac SET mac_id=%s WHERE mac_id=%s"
        cursor.execute(query, (new_mac, mac))
        connection.commit()
    finally:
        cursor.close()
        connection.close()

def login(username, passcode):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = "SELECT * FROM registered_mac WHERE user_name=%s AND pass_code=%s"
        cursor.execute(query, (username, passcode))
        result = cursor.fetchone()
        return result is not None
    finally:
        cursor.close()
        connection.close()

def profile():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        query = '''
        SELECT 
            stud_det.name, 
            stud_det.year, 
            stud_det.course, 
            stud_det.section, 
            stud_det.mac_id,
            registered_mac.user_name, 
            registered_mac.pass_code
        FROM 
            stud_det
        INNER JOIN 
            registered_mac ON stud_det.mac_id = registered_mac.mac_id
        '''
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            dataset = {
                'name': result[0],
                'year': result[1],
                'course': result[2],
                'section': result[3],
                'mac_id': result[4],
                'roll-no': result[5],
                'pass_code': result[6]
            }

            query = "SELECT sys_name, os_name FROM system WHERE mac_id=%s"
            cursor.execute(query, (dataset['mac_id'],))
            sys_info = cursor.fetchone()
            if sys_info:
                dataset['sys_name'] = sys_info[0]
                dataset['os'] = sys_info[1]

            return dataset
        return None
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    data = login('22csr207', 'kongu@2024')
    print(data)
