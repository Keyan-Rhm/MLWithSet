from itertools import product
from itertools import permutations
from itertools import combinations
from random import sample

a = ["g", "p", "r"]
b = ["d", "s", "o"]
c = ["0", "1", "2"]
d = ["1", "2", "3"]

e = list(product(a, b, c, d))
print len(e)

memes = list(permutations(e,3))
print(len(memes))
print memes[1000]


cards = filter(
    lambda _: all(
        [
            # look at all unique values of each property and see if there is 1 or 3
            len(set([a[i] for a in _])) in {1,3} for i in range(4)
        ]
    )
    ,
    memes
)

print len(cards)
print cards[456]