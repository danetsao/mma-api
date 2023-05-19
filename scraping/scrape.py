import idna
from numpy import double
import requests
from bs4 import BeautifulSoup
from waiting import wait


def get_athlete_data(name_postfix: str):
    print('Getting data for ' + name_postfix)
    url = 'https://www.ufc.com/athlete/' + name_postfix 
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    athlete_data = soup.find_all("div", class_='stats-records stats-records__container stats-records--one-column')


    athlete_data = athlete_data[0].text.split()

    wins_by_knockout = athlete_data[0]
    wins_by_submission = athlete_data[4]
    first_round_finishes = athlete_data[8]

    

    deep_stats = soup.find_all("dd", class_="c-overlap__stats-value")
    sig_strikes_landed = int(deep_stats[0].text)
    sig_strikes_attempted = int(deep_stats[1].text)
    striking_accuracy = int(sig_strikes_landed) / int(sig_strikes_attempted)
    # rounded two decimal places
    striking_accuracy = round(striking_accuracy, 2)

    take_downs_landed = deep_stats[2].text
    take_downs_attempted = deep_stats[3].text
    take_down_accuracy = int(take_downs_landed) / int(take_downs_attempted) * 100 
    # rounded two decimal places
    take_down_accuracy = round(take_down_accuracy, 2)

    stats_per_min = soup.find_all("div", class_="c-stat-compare__number")
    

    sig_strikes_landed_per_min = stats_per_min[0].text.split()[0]
    sig_strikes_absorbed_per_min = stats_per_min[1].text.split()[0]
    take_down_avg_per_15_min = stats_per_min[2].text.split()[0]
    submission_avg_per_15_min = stats_per_min[3].text.split()[0]
    
    sig_strikes_defense = stats_per_min[4].text.split()[0]
    take_down_defense = stats_per_min[5].text.split()[0]
    kockdown_avg = stats_per_min[6].text.split()[0]
    average_fight_time = stats_per_min[7].text.split()[0]
    
    stats_record_inner = soup.find_all("div", class_="stats-records-inner")

    sig_strikes_by_pos = soup.find_all("div", class_="c-stat-3bar__group")

    sig_strikes_standing = sig_strikes_by_pos[0].text.split()[1]
    sig_strikes_clinch = sig_strikes_by_pos[2].text.split()[1]
    sig_strikes_ground = sig_strikes_by_pos[4].text.split()[1]

    sig_strike_target = soup.find_all("text", id="e-stat-body_x5F__x5F_head_value")
    sig_strike_head = (sig_strike_target[0]).text

    sig_strike_target = soup.find_all("text", id="e-stat-body_x5F__x5F_body_value")
    sig_strike_body = (sig_strike_target[0]).text

    sig_strike_target = soup.find_all("text", id="e-stat-body_x5F__x5F_leg_value")
    sig_strike_leg = (sig_strike_target[0]).text

    win_methods = soup.find_all("div", class_="c-stat-3bar__value")

    wins_by_knockout = win_methods[3].text.split()[0]
    wins_by_submission = win_methods[4].text.split()[0]
    wins_by_decision = win_methods[5].text.split()[0]

    # Past fights


    #print all the stats and make sure we are right
    print(f'Wins by knockout: {wins_by_knockout}')
    print(f'Wins by submission: {wins_by_submission}')
    print(f'First round finishes: {first_round_finishes}')
    print(f'Significant strikes landed: {sig_strikes_landed}')
    print(f'Significant strikes attempted: {sig_strikes_attempted}')
    print(f'Striking accuracy: {striking_accuracy}')
    print(f'Take downs landed: {take_downs_landed}')
    print(f'Take downs attempted: {take_downs_attempted}')
    print(f'Take down accuracy: {take_down_accuracy}')
    print(f'Significant strikes landed per minute: {sig_strikes_landed_per_min}')
    print(f'Significant strikes absorbed per minute: {sig_strikes_absorbed_per_min}')
    print(f'Take down average per 15 minutes: {take_down_avg_per_15_min}')
    print(f'Submission average per 15 minutes: {submission_avg_per_15_min}')
    print(f'Significant strikes defense: {sig_strikes_defense}')
    print(f'Take down defense: {take_down_defense}')
    print(f'Kockdown average: {kockdown_avg}')
    print(f'Average fight time: {average_fight_time}')
    print(f'Significant strikes standing: {sig_strikes_standing}')
    print(f'Significant strikes clinch: {sig_strikes_clinch}')
    print(f'Significant strikes ground: {sig_strikes_ground}')
    print(f'Significant strikes head: {sig_strike_head}')
    print(f'Significant strikes body: {sig_strike_body}')
    print(f'Significant strikes leg: {sig_strike_leg}')
    print(f'Wins by KO/TKO: {wins_by_knockout}')
    print(f'Wins by decision: {wins_by_decision}')
    print(f'Wins by submission: {wins_by_submission}')

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
            print(name)
            rank_change = cells[2].text
            name_postfix = name.lower().replace(' ', '-').replace('.', '')
            current_athlete_data = {}
            try:
                current_athlete_data = wait(lambda: get_athlete_data(name_postfix), timeout_seconds=10, waiting_for="something to be ready")
            except Exception as e:
                print("Error: %s" % e)

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
    get_athlete_data('aljamain-sterling')