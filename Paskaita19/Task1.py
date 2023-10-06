def sum_of_numbers_list(numbers_list):
    total_sum = sum(numbers_list)
    return total_sum

def find_highest_number(*args):
    highest_number = max(args)
    return highest_number

def prime_numbers(n):
    if n < 1:
        return "Nera pirminis"
    for i in range(2, n):
        if(n % i) == 0:
            return "Nera pirminis"
    return "Pirminis"

