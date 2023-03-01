import random
import matplotlib.pyplot as plt


y = []
for exp in range(100000):
    # 100 random variable ranging from 1 to 100
    dummy = [random.choice(range(1, 101)) for x in range(100)]
    y.append(sum(dummy))

plt.hist(y, bins=100)
plt.show()
