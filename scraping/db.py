from link import post_title_list
from bs4 import BeautifulSoup
import requests
import psycopg2
from scrape import *

# Database connection info
HOST = "localhost"
USERNAME = "postgres"
PASSWORD = "root"
DATABASE = "data_db"

# Main function
def main():
    db = psycopg2.connect(host=HOST, user=USERNAME, password=PASSWORD, database=DATABASE)
    cursor = db.cursor()

    athlete_data = get_athlete_rankings()

    # Config and add to database

    db.commit()


if __name__ == "__main__":
    main()