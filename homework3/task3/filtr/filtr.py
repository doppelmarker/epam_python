class Filter:
    """
    Helper filter class. Accepts a list of single-argument
    functions that return True if object in list conforms to some criteria
    """

    def __init__(self, functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(f(item) for f in self.functions)]


positive_even = Filter([lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)])
print(positive_even.apply(range(-100, 100)))


def make_filter(**keywords):
    """
    Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():

        def wrapper(key=key, value=value):
            def keyword_filter_func(item):
                try:
                    return item[key] == value
                except KeyError:
                    return False

            return keyword_filter_func

        filter_funcs.append(wrapper())
    return Filter(filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": False, "kind": "parrot", "type": "bird", "name": "polly"},
    {"is_dead": False, "salary": 999999, "type": "Senior", "name": "Mark"},
]


new_filter = make_filter(is_dead=False)
print(new_filter.apply(sample_data))
