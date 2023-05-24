import idna
from numpy import double
import requests
from bs4 import BeautifulSoup
from waiting import wait


def get_athlete_data(name_postfix: str, print_data: bool = False) -> dict:
    print(f"Getting data for {name_postfix}")
    url = 'https://www.ufc.com/athlete/' + name_postfix 
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    athlete_data = soup.find_all("div", class_='stats-records stats-records__container stats-records--one-column')

    athlete_data = athlete_data[0].text.split()

    wins_by_knockout = athlete_data[0]
    wins_by_submission = athlete_data[4]
    try:    
        first_round_finishes = athlete_data[8]
    except IndexError:
        first_round_finishes = -1


    deep_stats = soup.find_all("dd", class_="c-overlap__stats-value")
    try:
        sig_strikes_landed = float(deep_stats[0].text)
    except ValueError:
        sig_strikes_landed = -1
    try:
        sig_strikes_attempted = float(deep_stats[1].text)
    except ValueError:
        sig_strikes_attempted = -1
    try:
        striking_accuracy = float(sig_strikes_landed) / float(sig_strikes_attempted)
    except ValueError:
        striking_accuracy = -1

    # rounded two decimal places
    striking_accuracy = round(striking_accuracy, 2)

    take_downs_landed = deep_stats[2].text
    take_downs_attempted = deep_stats[3].text
    try:
        take_down_accuracy = float(take_downs_landed) / float(take_downs_attempted) * 100 
    except ValueError:
        take_down_accuracy = -1
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

    #print(win_methods)

    wins_by_knockout = win_methods[3].text.split()[0]
    wins_by_decision = win_methods[4].text.split()[0]
    wins_by_submission = win_methods[5].text.split()[0]

    # Past fights
    fight_data = get_fight_data(name_postfix, print_data)

    if print_data:
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


    # config the vairbles into json format

    return {
        'wins_by_knockout': wins_by_knockout,
        'wins_by_submission': wins_by_submission,
        'first_round_finishes': first_round_finishes,
        'sig_strikes_landed': sig_strikes_landed,
        'sig_strikes_attempted': sig_strikes_attempted,
        'striking_accuracy': striking_accuracy,
        'take_downs_landed': take_downs_landed,
        'take_downs_attempted': take_downs_attempted,
        'take_down_accuracy': take_down_accuracy,
        'sig_strikes_landed_per_min': sig_strikes_landed_per_min,
        'sig_strikes_absorbed_per_min': sig_strikes_absorbed_per_min,
        'take_down_avg_per_15_min': take_down_avg_per_15_min,
        'submission_avg_per_15_min': submission_avg_per_15_min,
        'sig_strikes_defense': sig_strikes_defense,
        'take_down_defense': take_down_defense,
        'kockdown_avg': kockdown_avg,
        'average_fight_time': average_fight_time,
        'sig_strikes_standing': sig_strikes_standing,
        'sig_strikes_clinch': sig_strikes_clinch,
        'sig_strikes_ground': sig_strikes_ground,
        'sig_strike_head': sig_strike_head,
        'sig_strike_body': sig_strike_body,
        'sig_strike_leg': sig_strike_leg,
        'wins_by_knockout': wins_by_knockout,
        'wins_by_decision': wins_by_decision,
        'wins_by_submission': wins_by_submission,
        'fights': fight_data
    }


def get_fight_data(name_postfix: str, print_data: bool):
    #print('Getting fights for ' + name_postfix)
    url = 'https://www.ufc.com/athlete/' + name_postfix 

    last = name_postfix.split('-')[1]

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    fights = soup.find_all("div", class_="c-card-event--athlete-results__info")

    list_of_fights = []
    winners = soup.find_all("div", class_="c-card-event--athlete-results__red-image")

    list_of_winners = []

    list_of_winners_bool = [False] * len(winners)

    #find add the a tags within in winners to a list
    for i, winner in enumerate(winners):
        list_of_winners.append(winner.find("a"))

    for winner in list_of_winners:
        # if url is in winner
        if url in winner['href']:
            list_of_winners_bool[i] = True
    
    for i, fight in enumerate(fights):
        current_fight_result = fight.text.split()

        round = "Not found"
        time = "Not found"
        method = "Not found"
        win = list_of_winners_bool[i]

        opponent = current_fight_result[2]
        # The athlete's are listed on different sides based on who is ranked higher I believe
        if opponent.lower() == last:
            opponent = current_fight_result[0]
            if win:
                win = False
            else:
                win = True
        month = current_fight_result[3]
        day = current_fight_result[4]
        year = current_fight_result[5]

        if len(current_fight_result) > 6:
            round = current_fight_result[7]
            time = current_fight_result[9]
            method = current_fight_result[11]

        if print_data:
            print(f'Opponent: {opponent}')
            print(f'Win: {win}')
            print(f'Round: {round}')
            print(f'Time: {time}')
            print(f'Method: {method}')
            print(f'Month: {month}')
            print(f'Day: {day}')
            print(f'Year: {year}')
            print()


        current_fight_json = {
            'opponent': opponent,
            'win': win,
            'round': round,
            'time': time,
            'method': method,
            'month': month,
            'day': day,
            'year': year
        }
        list_of_fights.append(current_fight_json)
        
    return list_of_fights

def get_all_athletes(print_data: bool = False):
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
            name_postfix = name.lower().replace(' ', '-').replace('.', '')
            name_postfix = name_postfix[0:len(name_postfix)-1]
            current_athlete_data = {}

            if print_data:
                print(f'Weightclass: {ranking_name}')
                print(f'Name: {name}')
                print(f'Rank: {rank}')
                print(f'Rank Change: {rank_change}')

            try:
                current_athlete_data = wait(lambda: get_athlete_data(name_postfix, print_data), timeout_seconds=10, waiting_for="something to be ready")
            except Exception as e:
                print("Error: %s" % e)

            current_athlete_json = {
                'name': name,
                'rank': rank,
                'rank_change': rank_change,
                'weightclass': ranking_name,
                'data': current_athlete_data
            }



            list_of_athletes.append(current_athlete_json)
        
        list_of_classes.append(list_of_athletes)

    # Print the data to see what it looks like
    
    return list_of_classes



if __name__ == "__main__":
    get_all_athletes()