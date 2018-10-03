class Unique(object):
    _index = -1

    def __init__(self, items, **kwargs):
        if 'ignore_case' in kwargs.keys():
            if kwargs['ignore_case'] == True:
                items = list(map(lambda x: x.lower(), list(items)))
        self._uniq_items = list(set(items))

    def __next__(self):
        self._index += 1
        if self._index == len(self._uniq_items):
            raise StopIteration
        return self._uniq_items[self._index]

    def __iter__(self):
        return self
