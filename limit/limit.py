def limit(lists , min=None , max=None):
    min_check = lambda value : True if min is None else (value >= min)
    max_check = lambda value : True if max is None else (value <= max)

    return [value for value in lists if min_check(value) and max_check(value)]

print(limit([12,5,26,3,59,60,346,34,6,346], min=12,max=60))