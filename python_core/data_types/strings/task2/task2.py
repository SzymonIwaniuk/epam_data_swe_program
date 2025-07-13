def get_longest_word( s: str) -> str:
    strings = s.split()

    return max(strings, key=lambda word: len(word))

