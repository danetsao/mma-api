import requests
from bs4 import BeautifulSoup

def get_athlete_rankings():
    """
    Get the UFC athlete rankings from the UFC website.
    Currently prints top 15 athletes in each weight class, their ranking and their rank change.
    """

    url = 'https://www.ufc.com/rankings'
    response = requests.get(url)


    soup = BeautifulSoup(response.content, 'html.parser')

    rankings_data_raw = soup.find_all("div", class_='view-grouping')



    for rankings_table in rankings_data_raw:

        current_table = rankings_table.find("tbody", class_='')
        ranking_name = rankings_table.find("h4", class_='')

        print(ranking_name.text.strip())
        
        for current_athlete in current_table:

            print(current_athlete.text.strip())

