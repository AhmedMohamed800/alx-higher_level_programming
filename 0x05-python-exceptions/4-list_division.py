#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list = []
    add_element = 0
    for i in range(0, list_length):
        try:
            add_element = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            print("division by 0")
        except (TypeError):
            print("wrong type")
        except (IndexError):
            print("out of range")
        finally:
            my_list.append(add_element)
            add_element = 0
    return my_list
