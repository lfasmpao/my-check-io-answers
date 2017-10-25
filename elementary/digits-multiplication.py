def checkio(number):
    key = [int(x) for x in str(number) if x != str('0')]
    result = 1
    for i in key:
        result *= i
    return result


if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
