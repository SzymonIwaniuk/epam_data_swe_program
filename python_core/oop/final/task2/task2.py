class Cipher:
    def __init__(self, keyword):
        keyword = keyword.lower()
        seen = set()
        self.plain = "abcdefghijklmnopqrstuvwxyz"
        key_unique = "".join([c for c in keyword if not (c in seen or seen.add(c))])
        remaining = "".join([c for c in self.plain if c not in key_unique])
        self.cipher = key_unique + remaining

        self.encode_map = str.maketrans(self.plain, self.cipher)
        self.decode_map = str.maketrans(self.cipher, self.plain)

    def encode(self, data):
        return data.lower().translate(self.encode_map).capitalize() if data else ""

    def decode(self, data):
        return data.lower().translate(self.decode_map).capitalize() if data else ""
