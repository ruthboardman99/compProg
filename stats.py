import statistics
import math 

def main():
    pass

def get_count(teams, random = False):
    """Computes the count of elements in each teams. 
   Returns a dictionary containing the number of teams with 0, 1, 2, 3 or 4
    cheaters."""
    a = {
        0: teams.count(0),
        1: teams.count(1), 
        2: teams.count(2), 
        3: teams.count(3), 
        4: teams.count(4)
    }
        
    return a


def conf_int(N):
    """Finds the mean value, along with the upper and lower confidence 
    intervals. Returns all three values. """
    for i in range(len(N)): 
        mean_val = statistics.mean(N)
        upper_CI = mean_val + 1.96 * (statistics.stdev(N)/math.sqrt(len((N))))
        lower_CI = mean_val - 1.96 * (statistics.stdev(N)/math.sqrt(len((N))))
    return mean_val, upper_CI, lower_CI

if __name__ == '__main__':
    main()