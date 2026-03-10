import random

class Person():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.id = random.randint(1000,9999)
        self.friends = 0

    def __str__(self):
        return f"{self.first} {self.last}({self.id}) Friends: {self.friends}"

    def update_friends(self):
        self.friends += 1

def build_adjacency(data):
    adj_dict = dict()
    for node in data:
        a = node[0]
        b = node[1]
        if a in adj_dict:
            adj_dict[a].append(b)
        else:
            adj_dict[a] = [b]
        if b in adj_dict:
            adj_dict[b].append(a)
        else:
            adj_dict[b] = [a]

        a.update_friends()
        b.update_friends()
        
    return adj_dict

def displayAdj(adj_dict):
    for key, val in adj_dict.items():
        print(key)
        print("---")
        for i in val:
            print(i)
        print()

p1 = Person("Anita", "Racinez")
p2 = Person("Clem", "Jameson")
p3 = Person("Lars", "Eriksson")
p4 = Person("Jed", "Jones")
data = [(p1, p2), (p2, p3), (p1, p4), (p2, p4)]
displayAdj(build_adjacency(data))
