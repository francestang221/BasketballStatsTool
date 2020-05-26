"""
Python Development Techdegree
Project 2 - Basketball Stats Tool
--------------------------------
"""


import constants
import copy
import random

# make a copy of the original PLAYERS list and the TEAMS list
player_list = copy.deepcopy(constants.PLAYERS)
team_list = copy.deepcopy(constants.TEAMS)
num_players_team = int(len(player_list) / len(team_list))


def clean_data():
    # clean the heights
    for player in player_list:
        player['height'] = int(player['height'][0:3])

        # clean the experience levels
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False

        # clean the guardians field
        if 'and' in player['guardians']:
            player['guardians'] = player['guardians'].split(' and ')
        else:
            player['guardians'] = [player['guardians']]


# balance teams

def balance_teams(panthers, bandits, warriors):

    # create separate lists for experienced and inexperienced players
    exp_players = [player for player in player_list if player['experience']]
    inexp_players = [player for player in player_list if not player['experience']]

    def make_team(team_name):
        # assign 3 experienced players
        while len(exp_players) != 0 and len(team_name) < 3:
            team_name.append((exp_players.pop(random.randrange(len(exp_players)))))
        # assign 3 inexperienced players
        while len(inexp_players) != 0 and len(team_name) < 6:
            team_name.append(inexp_players.pop(random.randrange(len(inexp_players))))

    make_team(panthers)
    make_team(bandits)
    make_team(warriors)


# display total players, total experienced, total inexperienced, average height, guardians
def display_stats(team):
    # the number of experienced players on the team
    exp_num = len([player for player in team if player['experience']])
    # the number of inexperienced players on the team
    inexp_num = len([player for player in team if not player['experience']])

    # calculate the average height of the team
    total_height = 0
    for player in team:
        total_height += player['height']

    avg_height = round(total_height / len(team), 2)

    print('Team: Panthers Stats ')
    print('----------------------')
    print('Total Players: {}'.format(len(team)))
    print('Total Experienced: {}'.format(exp_num))
    print('Total Inexperienced: {}'.format(inexp_num))
    print('Average Height: {}'.format(avg_height))
    print('\nPlayers on Team: ')

    # Display names of the players
    player_names = []
    for player in team:
        player_names.append(player['name'])
    print(', '.join(player_names))

    # Display names of the guardians
    print('\nGuardians:')

    guardians = []
    for player in team:
        guardians.extend(player["guardians"])

    print(', '.join(guardians))


def display_menu():
    print("\nBASKETBALL TEAM STATS TOOL")
    print("\n", "--------MENU--------")
    print("\n Here are your choices: \n \n 1) Display Team Stats \n\n 2) Quit \n")


def main():
    clean_data()
    panthers = []
    bandits = []
    warriors = []
    balance_teams(panthers, bandits, warriors)

    display_menu()

    while True:

        user_option = input("Enter an option:  ")

        if user_option == "1":
            team_choice = input("\nPlease choose a team: \n \n 1) Panthers \n \n 2) Bandits \n \n 3) Warriors \n \n ")

            if team_choice == '1':
                display_stats(panthers)

            elif team_choice == '2':
                display_stats(bandits)

            elif team_choice == '3':
                display_stats(warriors)

            else:
                print("Oops! Not a valid option!")

            user_choice = input("\n \nPress 0 to quit or any other key to continue...\n")
            if user_choice == '0':
                print("\nHope you had fun! See you next time! ")
                break
            else:
                display_menu()

        elif user_option == '2':
            print("\nSee you next time!")
            break

        else:
            print("\nOops! Please enter 1 or 2. ")


if __name__ == "__main__":
    main()