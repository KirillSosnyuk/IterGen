nested_list = [
    {1, 2, 3, 3}, 
    {'a': 1, 'b': 2},
    ['a', 'b'],
	['a', 'b', [1, ['I love Python', 'hey', 0, -4], 2], 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class FlatIterator(list):
    def __init__(self, list_):
        self.list = list_.copy()
        self.working_list = []

    def __iter__(self):
        while any(filter(lambda x: isinstance(x, list), self.list)):
            for ind, item in enumerate(self.list):
                if isinstance(item, list):
                    self.working_list.extend(item)
                else:
                    self.working_list.append(item)
            self.list = self.working_list[:]
            self.working_list.clear()
        
        return iter(self.list)

    def __next__(self):
        return next(self.list)
        

        
if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item) 

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)