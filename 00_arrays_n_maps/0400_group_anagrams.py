from collections import defaultdict

def group(strs):
    res = defaultdict(list)

    for s in strs:
        count = [0]*26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)

    print(res)
    return list(res.values())

group(["act","pots","tops","cat","stop","hat"])

# cheated completely, understood but didnt solve

# it creates a dictionary or a tuple a-z representing 1 or 0
# [0000....] -> [word, word]
# [0000....] -> [word, word],
# optput all the words that are in values
