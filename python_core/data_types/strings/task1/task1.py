def get_fractions(a_b: str, c_b: str) -> str:
    splitted1 = a_b.split('/')
    splitted2 = c_b.split('/')

    res_top = str(int(splitted1[0]) + int(splitted2[0]))
    res_bot =  splitted2[1]

    return f"{a_b} + {c_b} = {res_top}/{res_bot}"

