n_items, d_eat = map(int, input().split())
items = [int(x) for x in input().split()]
anna_share = int(input())
anna = sum(items) - items[d_eat]
split = anna//2
if split == anna_share:
    print('Bon Appetit')
else:
    print(anna_share-split)
