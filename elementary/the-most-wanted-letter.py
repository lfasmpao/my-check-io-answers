def checkio(text):
    datas = [x for x in list(text.lower()) if x.isalpha()]
    result = dict.fromkeys(datas, 0)
    for i in range(len(datas)):
        result['{}'.format(datas[i])] += 1
    return sorted(result.items(), key=lambda k: (-k[1], k[0]))[0][0]


if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
