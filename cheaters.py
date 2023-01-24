def main():
    pass

def Teams(dictio):
    """Takes a dictionary as input and creates a new dictionary to
    control teams in each match. It checks if any players are marked as cheaters
    and assigns them to their respective teams. 
    Returns number of cheaters in each team. """
    # Copys original dictionary so it doesnt amend it. 
    diction = dictio.copy()
    
    # Create a teams dictionary 
    teams = {match + team: [] for match in diction.keys() for team in diction[match]['team_id']}
    for match in diction.keys():
        for team, player in zip(diction[match]["team_id"], diction[match]["cheater_dummy"]):
            key = match + team
            # Adds cheating accounts to dictionary. 
            teams[key].append(player)
    
    # Sums the number of cheaters in each team. 
    teams = [sum(x) for x in teams.values()]
    
    return teams


from copy import deepcopy

def killerCheated(dictio, cheater_id, first_cheated):
    """Takes a dictionary as input. Finds out whether an account is a
    cheater before they kill the account who is not a cheater.
    Returns the same dictionary but with the variable killer_is_cheat with values 1
    (cheat) and 0 (none cheat). """
    # Copy the dictionary so the original isn't modified.
    diction = deepcopy(dictio)
    cheater_set = set(cheater_id)
    first_cheated_dict = dict(zip(cheater_id, first_cheated))
    
    for match in diction:
        diction[match]['killer_is_cheat'] = []
        
        # Sets the conditions.
        for killed, killer, time in zip(diction[match]["killed_id"],diction[match]["killer_id"], diction[match]["time"]):
            # If the killer is cheater before they killed the other player. 
            if killer in cheater_set:
                if time >= first_cheated_dict[killer]:
                    diction[match]['killer_is_cheat'].append(1)
                else:
                    diction[match]['killer_is_cheat'].append(0)
            else:
                diction[match]['killer_is_cheat'].append(0)
    return diction


def KilledCheated(dictio, cheater_id, first_cheated):
    """Takes a dictionary as input. Finds out whether an account who was killed by a
    cheater becomes a cheater after being killed.
    Returns the same dictionary but with the variable killed_is_cheat with values 1
    (cheat) and 0 (none cheat).
    """
    # Copy the dictionary so the original isn't modified.
    diction = deepcopy(dictio)
    cheater_set = set(cheater_id)
    first_cheated_dict = dict(zip(cheater_id, first_cheated))
    
    for match in diction:
        diction[match]['killed_is_cheat'] = []
        
        # Sets the conditions.
        for killed, killer_cheater, time in zip(diction[match]["killed_id"], diction[match]["killer_is_cheat"], diction[match]["time"]):
            # Accounts killer must be a cheater. 
            if killer_cheater == 1: 
                # Account killed must be in cheater list.
                if killed in cheater_set:
                    # Killed account must not be a cheater when they are killed. 
                    if time < first_cheated_dict[killed]:
                        diction[match]['killed_is_cheat'].append(1)
                    else:
                        diction[match]['killed_is_cheat'].append(0)
                else:
                    diction[match]['killed_is_cheat'].append(0)
            else:
                diction[match]['killed_is_cheat'].append(0)
                
    return diction


def KilledThree(dictio, cheater_id, first_cheated):
    """Takes a dictionary as input. Finds out whether an account is a
    cheater and killed at least three people before they kill the account who is not
    a cheater. Then finds out if the killed person becomes a cheater aftwards. 
    Returns a list of how accounts who this refers to."""
    # Copy the dictionary so the original isn't modified.  
    diction = deepcopy(dictio)
    new_cheaters = []
    for match in diction.keys():
        i = -1
        # Sorts the variables 
        diction[match]["time"].sort()
        diction[match]["killed_id"] = [x for _, x in sorted(zip(diction[match]["time"], diction[match]["killed_id"]))]
        diction[match]["killer_id"] = [x for _, x in sorted(zip(diction[match]["time"], diction[match]["killer_id"]))]
        
        # Sets the conditions for accounts that need to be included in the new list. 
        for killed, killer, time in zip(diction[match]["killed_id"], diction[match]["killer_id"], diction[match]["time"]):
            i += 1
            killer_count = diction[match]['killer_id'][0:i+1].count(killer)
            if killer_count == 3:
                if killer in cheater_id:
                    index = cheater_id.index(killer)
                    if time >= first_cheated[index]:
                        break
        
        # Subsets the data.
        subset_victims = diction[match]['killed_id'][i+2:]
        time_killed = diction[match]['time'][i+2:]
        n = 0
        for killed in subset_victims: 
            if killed in cheater_id:
                index_killed = cheater_id.index(killed)
                if time_killed[n] <= first_cheated[index_killed]:
                    new_cheaters.append(diction[match]["killed_id"][i])

    return new_cheaters



if __name__ == '__main__':
    main()