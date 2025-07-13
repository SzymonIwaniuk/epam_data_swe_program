def replacer(s: str) -> str:
    res = ''

    for char in s:
        if char == "'":
            res += '"'
        elif char == '"':
            res += "'"
        else:
            res += char
            
    return res


