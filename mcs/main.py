# This is sample in Python for
# Most Common (Even/Uneven) Sum of given list

# Press Shift+F10 to execute it.

def get_biggest_even_sum(list_numbers, var_size):
    # Use a breakpoint in the code line below to debug your script.
    list_numbers.sort(reverse=True)
    list_numbers_length = len(list_numbers)
    list_chosen_numbers = []
    var_biggest_even_sum = 0
    var_is_even_sum_found = False
    var_starting_pos = 0
    while 1:
        list_chosen_numbers = []
        var_index = var_starting_pos
        var_current_sum = 0
        while var_index < var_size - 1:
            var_current_sum += list_numbers[var_index]
            list_chosen_numbers.append(list_numbers[var_index])
            var_index += 1
        while var_index < list_numbers_length:
            var_number = list_numbers[var_index]
            var_test_sum = var_current_sum + var_number
            if var_test_sum % 2 == 0:
                var_biggest_even_sum = var_test_sum
                var_is_even_sum_found = True
                break
            var_index += 1
        if not var_is_even_sum_found:
            var_starting_pos += 1
        else:
            break
