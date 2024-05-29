#!/home/sudharsan/myenv/bin/python3
import mysql.connector 
from dotenv import load_dotenv
import os

def check(mac):

    load_dotenv()

    pass_key = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pass_key,
        database=db_name
    )

    mycursor = mydb.cursor()

    query = "SELECT * FROM registered_mac WHERE mac_id=%s"
    mycursor.execute(query, (mac,))
    result = mycursor.fetchone()  
    mydb.close()
    if result:
        return True
    else:
        return False


    
