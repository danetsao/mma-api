from link import post_title_list
from bs4 import BeautifulSoup
import requests
import psycopg2
from scrape import *

HOST = "localhost"
USERNAME = "postgres"
PASSWORD = "root"
DATABASE = "data_db"

db = psycopg2.connect(host=HOST, user=USERNAME, password=PASSWORD, database=DATABASE)
cursor = db.cursor()

athlete_data = get_athlete_rankings()

# Config and add to database


db.commit()
