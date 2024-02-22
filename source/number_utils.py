from source.magnanimous_numbers import is_magnanimous


def list_numbers(count) -> [int]:
    """
    return a list of the nth magnanimous numbers
    :param count:
    """
    found = 0
    candidate = 0
    result = []
    while found < count:
        if is_magnanimous(candidate):
            result.append(candidate)
            found += 1
        candidate += 1
    
    return result


def find_between(start, end):
    """
    Return a list of magnanimous numbers in the range given
    :param start: the Nth Magnanimous number to start from
    :param end: the Nth Magnanimous number to end at
    :return: list of the numbers found
    
    find_between(5,10) will return a list of the 5th, 6th,7th, 8th,9th & 10th magnanimous numbers
    [4, 5, 6, 7, 8, 9]
    """
    
    result = []
    number = 0
    count = 0
    
    count, number = skip_to_start(count, number, start)
    
    result.append(number)
    number += 1  # move to next number
    
    collect_numbers(count, end, number, result)
    return result


def collect_numbers(count, end, number, result):
    while count < end:
        if is_magnanimous(number):
            print(number)
            result.append(number)
            count += 1
        if count != end: number += 1


def skip_to_start(count, number, start):
    # skip to start
    while count < start:
        if is_magnanimous(number):
            count += 1
        if count != start: number += 1
    return count, number
