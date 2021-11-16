words = []


def check(word):
    return if word in words


def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        words.append(line.rstrip())
    return True


def size():
    n = 0
    for word in words:
        n += 1
    return n


def unload():
    return True
