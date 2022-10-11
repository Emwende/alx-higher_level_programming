#!/usr/bin/python3

"""a function that prints the first x
elements of a list and only integers."""
Args:
    my_list(list): The list to print elements from.
    x(int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
        """
        ret = 0
        for i in range(x):
        try:
        print("{}".format(my_list[i]), end="")
        ret += 1
        except IndexError:
        break
        print("")
        return (ret)
