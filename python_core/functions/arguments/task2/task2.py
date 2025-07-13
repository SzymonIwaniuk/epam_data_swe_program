def union(*args) -> set:
    result = set()
    for arg in args:
        result |= set(arg)
    return result


def intersect(*args) -> set:
    result = set(args[0])
    for arg in args[1:]:
        result &= set(arg)
    return result

