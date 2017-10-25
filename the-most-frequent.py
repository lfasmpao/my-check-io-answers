def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    return sorted(data, key=data.count, reverse=True)[0]


if __name__ == '__main__':
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
