from collections import OrderedDict
ordinary_dict = {}
ordinary_dict['a'] = 1
ordinary_dict['b'] = 2
ordinary_dict['c'] = 3
ordinary_dict['d'] = 4
ordinary_dict['e'] = 5
# this may be in orbitrary order prior to Python 3.7
print(ordinary_dict)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)
# same functionality as with ordinary dict, but always ordered
for k, v in ordinary_dict.items():
    print(k, v)a