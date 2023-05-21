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
    athlete_data = get_all_athletes()

    # Config and add to database
    # make an extremely basic query to test the connection, just insert a 1 and make a new table
    cursor.execute("INSERT INTO test (id) VALUES (1);")
    
    db.commit()


if __name__ == "__main__":
    main()