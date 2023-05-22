import os, sys
from bs4 import BeautifulSoup
import requests
import psycopg2

sys.path.append('../')

from scrape import *

# Database connection constants
HOST = os.environ.get('DB_HOST')
PORT = os.environ.get('DB_PORT')
USERNAME = os.environ.get('DB_USERNAME')
PASSWORD = os.environ.get('DB_PASSWORD')
DATABASE = os.environ.get('DB_NAME')

# Main function
def main():


    print('Getting all athletes...')
    athlete_data = get_athlete_data('leon-edwards')

    #establishing the connection
    conn = psycopg2.connect(
    database=DATABASE, user=USERNAME, password=PASSWORD, host=HOST, port=PORT)
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a database
    sql = '''CREATE database mydb''';

    #Creating a database
    cursor.execute(sql)
    print("Database created successfully........")

    #Closing the connection
    conn.close()

if __name__ == "__main__":
    main()