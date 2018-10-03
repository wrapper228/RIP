import random


def field(items, *args):
    for i in items:
        dct = {}
        for arg in args:
            if (len(args) == 1) and (arg in i.keys()):
                if i[arg]:
                    yield i[arg]
            elif (len(args) > 1) and (arg in i.keys()):
                if i[arg]:
                    dct[arg] = i[arg]
        if dct:
            yield dct

def gen_random(begin, end, num_count):
    for _ in range(num_count):
        yield random.randint(begin, end)
