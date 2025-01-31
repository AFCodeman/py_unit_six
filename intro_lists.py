def swap(list_one):
    """
    Function that swaps the first and last elements of the list, regardless of length
    :param list_one: a list of at least two elements
    :return: the same list with the first and last elements swapped
    """
    x=list_one[0]
    list_one[0]=list_one[-1]
    list_one[-1]=x
    return list_one

def rotate_left(list_one):
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
    :param list_one: A list consisting of exactly three integers
    :return: a list where all the elements have been shifted 1 place to the left
    """
    x=list_one[0]
    y=list_one[1]
    z=list_one[2]
    list_one[0]=list_one[1]
    list_one[1]=z
    list_one[2]=x
    return list_one


def max_end(list_one):
    """
    This function will find if the first or last element of an list is larger, then set all the elements
    of that list to that value.
    :param list_one: A list consisting of three elements - all integers
    :return: A list where all the elements are the larger of the first or last element of the original list
    """
    x=list_one[0]
    y=list_one[-1]
    if x>y:
        list_one[0]=x
        list_one[1]=x
        list_one[-1]=x
        return list_one
    elif x<y:
        list_one[0]=y
        list_one[1]=y
        list_one[-1]=y
        return list_one
    else:
        return list_one[0:-1]