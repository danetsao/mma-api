import requests
from bs4 import BeautifulSoup

def get_athlete_data(name_postfix: str):
    url = 'https://www.ufc.com/athlete/' + name_postfix 
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    return {'wins':'1'}

def get_athlete_rankings():
    """
    Get the UFC athlete rankings from the UFC website.
    Currently prints top 15 athletes in each weight class, their ranking and their rank change.
    """

    url = 'https://www.ufc.com/rankings'
    response = requests.get(url)


    soup = BeautifulSoup(response.content, 'html.parser')

    rankings_data_raw = soup.find_all("div", class_='view-grouping')

    list_of_classes = []

    for rankings_table in rankings_data_raw:
        list_of_athletes = []
        current_table = rankings_table.find("tbody", class_='')
        ranking_name = rankings_table.find("h4", class_='')
        ranking_name = ranking_name.text

        for current_athlete in current_table.find_all('tr'): # Loop through each table row
            cells = current_athlete.find_all('td') # Find all cells in the row

            rank = cells[0].text
            name = cells[1].text
            rank_change = cells[2].text
            name_postfix = 'leon-edwards'
            current_athlete_data = get_athlete_data(name_postfix)

            current_athlet_list = [ranking_name, name, rank, rank_change, current_athlete_data]


            list_of_athletes.append(current_athlet_list)
        
        list_of_classes.append(list_of_athletes)

    # Print the data to see what it looks like
    for c in list_of_classes:
        if c:
            print(c[0][0])
        for a in c:
            print(a[2], a[1], a[3], a[4])
        print()


if __name__ == "__main__":
    get_athlete_rankings()