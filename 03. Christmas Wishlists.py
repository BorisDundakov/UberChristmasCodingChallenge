n_friends = int(input())
presents_list = [int(el) for el in input().split()]
minutes = 10080
res = 0
combos = [[]]
idx = 0
# TODO: izmisli cikula

import itertools

numbers = [1, 2, 3, 7, 7, 9, 10]
target = 10

result = [seq for i in range(len(presents_list), 0, -1)
          for seq in itertools.combinations(numbers, i)
          if sum(seq) <= minutes]

print(len(result))
