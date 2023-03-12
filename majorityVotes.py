def majority_votes(votes):
    """Returns the most common element in votes"""
    vote_count = {}
    for vote in votes:
        if vote in vote_count:
            vote_count[vote] += 1
        else:
            vote_count[vote] = 1

    maximum = max(vote_count.values())
    arr = {}
    for key, value in vote_count.items():
        if value == maximum:
            arr[key] = value
    return random.choice(list(arr.keys()))
  
  
  # more optimized way is to use scipy.stats.mstats.mode() 
