def main():
    pass

def cheaters(path):
    """Takes in a path and donwloads the data into lists. """
    # Creates empty lists. 
    cheater_id = []
    first_cheated = []
    banned = []
    # Iterates through data and asigns data to each list. 
    for line in open(path, 'r'):
        strlst = line.strip().split('\t')
        cheater_id.append(strlst[0])
        first_cheated.append(strlst[1])
        banned.append(strlst[2])
    
    return cheater_id, first_cheated, banned 

def team(path):
    """Takes in a path and donwloads the data into lists. """
    # Creates empty lists. 
    match_id = []
    player_id = []
    team_id = [] 
    # Iterates through data and asigns data to each list. 
    for line2 in open(path, 'r'):
        strlst = line2.strip().split('\t')
        match_id.append(strlst[0])
        player_id.append(strlst[1])
        team_id.append(strlst[2])
    
    return match_id, player_id, team_id

def kills(path):
    """Takes in a path and donwloads the data into lists. """
    # Creates empty lists. 
    match_ID = []
    killer_id = []
    killed_id = []
    time = []
    # Iterates through data and asigns data to each list. 
    for line3 in open(path, 'r'):
        strlst = line3.strip().split('\t')
        match_ID.append(strlst[0])
        killer_id.append(strlst[1])
        killed_id.append(strlst[2])
        time.append(strlst[3])
    
    return match_ID, killer_id, killed_id, time


def diction1(cheater_id, match_id, team_id, player_id):
    """Takes three lists as input. Makes a new variable called cheter_dummy,
    store the variables in a nested dictionary. Retruns the dictionary and
    new variable."""
    # Creates an empty dictionary. 
    diction = {match_id[x]: {"team_id":[], "cheater_dummy":[]} for x in range(len(match_id))}
    
    # Creates a cheater dummy. If player is a cheater, the result is 1, 0 if otherwise. 
    cheater_dummy = [1 if p in cheater_id else 0 for p in player_id]
    
    # Assigns data to the dictionary.    
    for match, team, player in zip(match_id, team_id, cheater_dummy):
        diction[match]['team_id'].append(team)
        diction[match]['cheater_dummy'].append(player)
        
    return diction, cheater_dummy


def diction2(match_ID, killed_id, killer_id, time):
    """Takes four lists as input.  Returns a nested dictionary."""
     # Creates an empty dictionary. 
    diction2 = {match_ID[x]: {"killed_id":[], "killer_id": [], "time": [], 'killer_is_cheat': [], 'killed_is_cheat': []} for x in range(len(match_ID))}
    
    # Assigns data to the dictionary. 
    for match, killed, killer, times in zip(match_ID, killed_id, killer_id, time):
        diction2[match]['killed_id'].append(killed)
        diction2[match]['killer_id'].append(killer)
        diction2[match]['time'].append(times)

    return diction2


def diction3(match_ID, killed_id, killer_id, time):
    """Takes four lists as input.  Returns a nested dictionary."""    
    # Creates an empty dictionary. 
    diction3 = {match_ID[x]: {"killed_id":[], "killer_id": [], "time": [], 'killer_is_cheat': [], 'killed_is_cheat': [], 'killed_three': []} for x in range(len(match_ID))}
    
    # Assigns data to the dictionary.
    for match, killed, killer, times in zip(match_ID, killed_id, killer_id, time):
        diction3[match]['killed_id'].append(killed)
        diction3[match]['killer_id'].append(killer)
        diction3[match]['time'].append(times)

    return diction3


if __name__ == '__main__':
    main()

