def flat_generator(mylist: list):
    new_list = []
    while any(filter(lambda x: type(x) == list, mylist)):
        for item in mylist:
            if isinstance(item, list):
                new_list.extend(item)
            else:
                new_list.append(item)

        mylist = new_list[:]
        new_list.clear()

    for item in mylist:
            yield item
        

nested_list = [
    {1, 2, 3, 3}, 
    {'a': 1, 'b': 2},
    ['a', 'b'],
	['a', 'b', [1, ['I love Python', 'hey', 0, -4], 2], 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

for item in flat_generator(nested_list):
	print(item)