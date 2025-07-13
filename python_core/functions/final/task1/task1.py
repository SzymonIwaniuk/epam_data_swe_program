from typing import List

#TODO
def split(data: str, sep=None, maxsplit=-1):
    if maxsplit == 0:
        if sep is None:
            stripped = data.strip()
            return [stripped] if stripped else []
        else:
            return [data]

    res = []

    if sep is None: 
        i = 0
        n = len(data)
        splits_done = 0

        while i < n:
            while i < n and data[i].isspace():
                i += 1
            if i >= n:
                break
            start = i
            while i < n and not data[i].isspace():
                i += 1
            res.append(data[start:i])
            splits_done += 1
            if 0 <= maxsplit == splits_done:
                break

        if 0 <= maxsplit == splits_done and i < n:
            while i < n and data[i].isspace():
                i += 1
            if i < n:
                res.append(data[i:])

    else:
        l = len(sep)
        prev = 0
        splits_done = 0

        while True:
            idx = data.find(sep, prev)
            if idx == -1 or (0 <= maxsplit == splits_done):
                break
            res.append(data[prev:idx])
            prev = idx + l
            splits_done += 1

        res.append(data[prev:])
    
    if sep is None and len(res) == 1 and res[0] == '':
        return []
        
    return res 


if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep=',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2     3', maxsplit=1) == ['Python', '2     3']
    assert split('    test     6    7', maxsplit=1) == ['test', '6    7']
    assert split('    Hi     8    9', maxsplit=0) == ['Hi     8    9']
    assert split('    set   3     4') == ['set', '3', '4']
    assert split('set;:23', sep=';:', maxsplit=0) == ['set;:23']
    assert split('set;:;:23', sep=';:', maxsplit=2) == ['set', '', '23']

