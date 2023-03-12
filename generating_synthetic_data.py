import scipy.stats as ss
import numpy as np


def generate_data(n=20):
    points = np.concatenate((ss.norm(0, 1).rvs((n, 2)), ss.norm(1, 1).rvs((n, 2))), axis=0)
    obs = np.concatenate((np.repeat(0, n), np.repeat(1, n)))
    return points, obs
