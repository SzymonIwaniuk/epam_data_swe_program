def union(*args) -> set:
    out = set()

    for data in args:
        out.update(set(data))

    return out


def intersect(*args) -> set:
    first = set(args[0])

    for next in args[1:]:
        first.intersection(set(next))

    return first

