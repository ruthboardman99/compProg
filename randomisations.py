from random import sample
from random import shuffle
from copy import deepcopy

def main():
    pass


def Randomisation1(diction):
    """ This function takes in a dictionary and randomly shuffles the
    'team_id' values for each match in the dictionary.
    The original dictionary is not modified, a copy of the dictionary is returned with
    the shuffled 'team_id' values.
    """
    # Copy the dictionary so the original isn't modified.
    diction_copy = diction.copy()
    for match in diction_copy.items():
        shuffle(diction_copy[match[0]]['team_id'])
    
    return diction_copy


def Randomisation2(dictio):
    """takes a dictionary as input. Merges the two account lists, shuffles them and
    then reassigns the suffled accounts back into the original list, whilst
    maintaining the structure. Returns the same dictionary. """
     # Copy the dictionary so the original isn't modified.
    diction = deepcopy(dictio)
    for match in diction.keys():
        # Puts the accounts in one list.
        match_players = diction[match]["killer_id"] + diction[match]["killed_id"]
        
         # Finds the index of each account. 
        for _ in range(len(match_players)):
            a, b = sample(match_players, 2)
            a_indices = [i for i, x in enumerate(diction[match]["killer_id"]) if x == a] + [i for i, x in enumerate(diction[match]["killed_id"]) if x == a]
            b_indices = [i for i, x in enumerate(diction[match]["killer_id"]) if x == b] + [i for i, x in enumerate(diction[match]["killed_id"]) if x == b]
            
            # Swaps accounts and reassigns them back into the lists.
            # Maintains the structure. 
            for a_index, b_index in zip(a_indices, b_indices):
                if a in diction[match]["killer_id"]:
                    diction[match]["killer_id"][a_index] = b
                else:
                    diction[match]["killed_id"][a_index] = b
                if b in diction[match]["killer_id"]:
                    diction[match]["killer_id"][b_index] = a
                else:
                    diction[match]["killed_id"][b_index] = a
    return diction



if __name__ == '__main__':
    main()