import random

def get_birthdays():
    list = []
    for x in range(24):
        x=random.randint(1, 366)
        list.append(x)
    return list

def is_duplicates(list):
    for x in range(len(list)-1):
        for y in range(x+1,24):
            if list[x]==list[y]:
                return True
    else:
        return False

def main ():
    number = int(input("How many more times would you like to run the program? "))
    sum = 0
    for x in range (number):
        list = get_birthdays()
        is_duplicates(list)
        if is_duplicates(list) == True:
            sum += 1
    print(sum/number)

if __name__ == '__main__':
    main()