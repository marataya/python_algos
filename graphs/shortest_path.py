'''
Example from Grokking Algorithms using BFS
'''

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(person):
    return person[-1] == 'm'


def search_mango_seller():
    search_queue = deque()
    search_queue += graph['you']
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


if __name__ == '__main__':
    search_mango_seller()
