def print_reversed_list_integer(my_list=[]):
    my_list = my_list[::-1]
    for i in range(len(my_list)):
        print("{:d}" .format(my_list[i]))
my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
