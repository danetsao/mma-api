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

# Thank to github copilot for helping me write these queries

# Main function
def main():


    print('Getting all athletes from data.json...')
    #set athlete data to the list of json objects from the file data.json
    with open('data.json', 'r', encoding='utf-8') as f:
        list_of_weight_classes = json.load(f)
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
            athlete = validate(athlete)
            try:
                cursor.execute(athlete_sql, (athlete['name'], athlete['rank'], athlete['data']['first_round_finishes'], athlete['data']['sig_strikes_landed'], athlete['data']['sig_strikes_attempted'], athlete['data']['striking_accuracy'], athlete['data']['take_downs_landed'], athlete['data']['take_downs_attempted'], athlete['data']['take_down_accuracy'], athlete['data']['sig_strikes_landed_per_min'], athlete['data']['sig_strikes_absorbed_per_min'], athlete['data']['take_down_avg_per_15_min'], athlete['data']['submission_avg_per_15_min'], athlete['data']['sig_strikes_defense'], athlete['data']['take_down_defense'], athlete['data']['kockdown_avg'], athlete['data']['average_fight_time'], athlete['data']['sig_strikes_standing'], athlete['data']['sig_strikes_clinch'], athlete['data']['sig_strikes_ground'], athlete['data']['sig_strike_head'], athlete['data']['sig_strike_body'], athlete['data']['sig_strike_leg'], athlete['data']['wins_by_knockout'], athlete['data']['wins_by_submission'], athlete['data']['wins_by_decision']))
                print(f'Inserted {athlete["name"]} into database')
            except Exception as e:
                print(f'Error inserting {athlete["name"]} into database')
    print("Database created successfully........")

    #Closing the connection
    conn.close()

def validate(athlete):
    if not athlete['data']:
        return athlete
    if athlete['data']['first_round_finishes'] == '':
        athlete['data']['first_round_finishes'] = 0
    if athlete['data']['sig_strikes_landed'] == '':
        athlete['data']['sig_strikes_landed'] = 0
    if athlete['data']['sig_strikes_attempted'] == '':
        athlete['data']['sig_strikes_attempted'] = 0
    if athlete['data']['striking_accuracy'] == '':
        athlete['data']['striking_accuracy'] = 0
    if athlete['data']['take_downs_landed'] == '':
        athlete['data']['take_downs_landed'] = 0
    if athlete['data']['take_downs_attempted'] == '':
        athlete['data']['take_downs_attempted'] = 0
    if athlete['data']['take_down_accuracy'] == '':
        athlete['data']['take_down_accuracy'] = 0
    if athlete['data']['sig_strikes_landed_per_min'] == '':
        athlete['data']['sig_strikes_landed_per_min'] = 0
    if athlete['data']['sig_strikes_absorbed_per_min'] == '':
        athlete['data']['sig_strikes_absorbed_per_min'] = 0
    if athlete['data']['take_down_avg_per_15_min'] == '':
        athlete['data']['take_down_avg_per_15_min'] = 0
    if athlete['data']['submission_avg_per_15_min'] == '':
        athlete['data']['submission_avg_per_15_min'] = 0
    if athlete['data']['sig_strikes_defense'] == '':
        athlete['data']['sig_strikes_defense'] = 0
    if athlete['data']['take_down_defense'] == '':
        athlete['data']['take_down_defense'] = 0
    if athlete['data']['kockdown_avg'] == '':
        athlete['data']['kockdown_avg'] = 0
    if athlete['data']['average_fight_time'] == '':
        athlete['data']['average_fight_time'] = 0
    if athlete['data']['sig_strikes_standing'] == '':
        athlete['data']['sig_strikes_standing'] = 0
    if athlete['data']['sig_strikes_clinch'] == '':
        athlete['data']['sig_strikes_clinch'] = 0
    if athlete['data']['sig_strikes_ground'] == '':
        athlete['data']['sig_strikes_ground'] = 0
    if athlete['data']['sig_strike_head'] == '':
        athlete['data']['sig_strike_head'] = 0
    if athlete['data']['sig_strike_body'] == '':
        athlete['data']['sig_strike_body'] = 0
    if athlete['data']['sig_strike_leg'] == '':
        athlete['data']['sig_strike_leg'] = 0
    if athlete['data']['wins_by_knockout'] == '':
        athlete['data']['wins_by_knockout'] = 0
    if athlete['data']['wins_by_submission'] == '':
        athlete['data']['wins_by_submission'] = 0
    if athlete['data']['wins_by_decision'] == '':
        athlete['data']['wins_by_decision'] = 0
    
    return athlete

if __name__ == "__main__":
    main()