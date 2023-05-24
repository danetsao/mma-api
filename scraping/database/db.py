import os, sys
from bs4 import BeautifulSoup
import requests
import psycopg2
import json

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


    print('Getting all athletes from data.json...')
    #set athlete data to the list of json objects from the file data.json
    list_of_weight_classes = get_all_athletes()
    #establishing the connection
    conn = psycopg2.connect(
    database=DATABASE, user=USERNAME, password=PASSWORD, host=HOST, port=PORT)
    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a database


    sql = '''CREATE TABLE IF NOT EXISTS top_fighters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    pound_for_pound_rank INTEGER,
    first_round_finishes INTEGER,
    sig_strikes_landed FLOAT,
    sig_strikes_attempted FLOAT,
    striking_accuracy FLOAT,
    take_downs_landed INTEGER,
    take_downs_attempted INTEGER,
    take_down_accuracy FLOAT,
    sig_strikes_landed_per_min FLOAT,
    sig_strikes_absorbed_per_min FLOAT,
    take_down_avg_per_15_min FLOAT,
    submission_avg_per_15_min FLOAT,
    sig_strikes_defense INTEGER,
    take_down_defense INTEGER,
    kockdown_avg FLOAT,
    average_fight_time VARCHAR(10),
    sig_strikes_standing INTEGER,
    sig_strikes_clinch INTEGER,
    sig_strikes_ground INTEGER,
    sig_strike_head INTEGER,
    sig_strike_body INTEGER,
    sig_strike_leg INTEGER,
    wins_by_knockout INTEGER,
    wins_by_submission INTEGER,
    wins_by_decision INTEGER
    )
    '''

    #Preparing query to insert data into table
    athlete_sql = 'INSERT INTO top_fighters (name, pound_for_pound_rank, first_round_finishes, sig_strikes_landed, sig_strikes_attempted, striking_accuracy, take_downs_landed, take_downs_attempted, take_down_accuracy, sig_strikes_landed_per_min, sig_strikes_absorbed_per_min, take_down_avg_per_15_min, submission_avg_per_15_min, sig_strikes_defense, take_down_defense, kockdown_avg, average_fight_time, sig_strikes_standing, sig_strikes_clinch, sig_strikes_ground, sig_strike_head, sig_strike_body, sig_strike_leg, wins_by_knockout, wins_by_submission, wins_by_decision) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)'

    #Creating a database
    cursor.execute(sql)

    #insert data into table, from list of json objects in data.json
    for weight_class in list_of_weight_classes:
        for athlete in weight_class:
            cursor.execute(athlete_sql, (athlete['name'], athlete['pound_for_pound'], athlete['first_round_finishes'], athlete['sig_strikes_landed'], athlete['sig_strikes_attempted'], athlete['striking_accuracy'], athlete['take_downs_landed'], athlete['take_downs_attempted'], athlete['take_down_accuracy'], athlete['sig_strikes_landed_per_min'], athlete['sig_strikes_absorbed_per_min'], athlete['take_down_avg_per_15_min'], athlete['submission_avg_per_15_min'], athlete['sig_strikes_defense'], athlete['take_down_defense'], athlete['kockdown_avg'], athlete['average_fight_time'], athlete['sig_strikes_standing'], athlete['sig_strikes_clinch'], athlete['sig_strikes_ground'], athlete['sig_strike_head'], athlete['sig_strike_body'], athlete['sig_strike_leg'], athlete['wins_by_knockout'], athlete['wins_by_submission'], athlete['wins_by_decision']))

    print("Database created successfully........")

    #Closing the connection
    conn.close()

if __name__ == "__main__":
    main()