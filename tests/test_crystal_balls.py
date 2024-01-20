from search.crystal_balls import crystal_balls
import random


def test_crystal_balls():
    idx = random.randint(0, 10000)
    data = [False] * 10000

    for i in range(idx, 10000):
        data[i] = True

    assert crystal_balls(data) == idx
    test_arr = [False] * 821
    assert crystal_balls(test_arr) == -1
