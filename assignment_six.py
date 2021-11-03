import random

def get_birthdays():
    list = []
    for x in range (23):
        x=random.randint(1, 366)
        list.append(x)
    return list

def is_duplicates(list):
    for x in range(22):
        list[x]
        for y in range (x+1,23):
            list[y]
        if list[x]==list[y]:
            return True