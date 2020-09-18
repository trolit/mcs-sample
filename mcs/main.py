# This is sample in Python language for
# MCS - Most Common (Even/Uneven) Sum
# for given list, size and mode
# created by https://github.com/trolit

# Press Shift+F10 to execute it.

# expected mode => even/uneven
def get_biggest_sum_depending_on_mode(list_numbers, var_size, var_mode):
    # Use a breakpoint in the code line below to debug your script.
    list_numbers_length = len(list_numbers)
    if var_size > list_numbers_length or var_size < 2 or var_mode != 'even' and var_mode != 'uneven':
        return
    list_numbers.sort(reverse=True)
    list_chosen_numbers = []
    var_biggest_sum = 0
    var_is_sum_found = False
    var_starting_pos = 0
    while 1:
        list_chosen_numbers = []
        var_index = var_starting_pos
        var_current_sum = 0
        var_number_counter = 0
        while var_number_counter < var_size - 1 and var_index < list_numbers_length:
            var_current_sum += list_numbers[var_index]
            list_chosen_numbers.append(list_numbers[var_index])
            var_index += 1
            var_number_counter += 1
        if var_number_counter + 1 != var_size:
            print('For: [', return_elements_of_list(list_numbers), ']')
            print(f'Couldn\'t find {var_size} numbers for mode: {var_mode}')
            print()
            break
        while var_index < list_numbers_length:
            var_number = list_numbers[var_index]
            var_test_sum = var_current_sum + var_number
            if (var_test_sum % 2 == 0 and var_mode == 'even') or (var_test_sum % 2 != 0 and var_mode == 'uneven'):
                list_chosen_numbers.append(var_number)
                var_biggest_sum = var_test_sum
                var_is_sum_found = True
                print('For: [', return_elements_of_list(list_numbers), '],', var_mode, '(', var_size, ')')
                print('selected:', return_elements_of_list(list_chosen_numbers))
                print('which gives:', var_biggest_sum)
                print()
                break
            var_index += 1
        if not var_is_sum_found:
            var_starting_pos += 1
        else:
            break
        if var_starting_pos >= list_numbers_length:
            print('For: [', return_elements_of_list(list_numbers), ']')
            print(f'var_starting_pos reached unexpected position {var_starting_pos}')
            print()
            break


def return_elements_of_list(user_list):
    var_list_elements = ''
    var_i = 0
    for list_item in user_list:
        if var_i == 0:
            var_list_elements += str(list_item)
        else:
            var_list_elements += ' ' + str(list_item)
        var_i += 1
    return var_list_elements


# Examples
get_biggest_sum_depending_on_mode([1, 2, 9, 3, 6, 6, 7, 7, 3], 4, 'even')
get_biggest_sum_depending_on_mode([102, 15, 33, 4, 81, 2, 13, 6, 79], 4, 'even')
get_biggest_sum_depending_on_mode([4, 32, 15, 1, 6, 2, 8, 6, 9], 3, 'uneven')
get_biggest_sum_depending_on_mode([0, 0, 3, 2, 0, 5, 2, 7, 6], 7, 'uneven')
get_biggest_sum_depending_on_mode([3, 32, 5], 3, 'uneven')
get_biggest_sum_depending_on_mode([3, 32, 5], 2, 'uneven')
get_biggest_sum_depending_on_mode([1, 1, 1, 2, 3], 3, 'uneven')
get_biggest_sum_depending_on_mode([6, 0, 0, 4, 3], 5, 'even')
