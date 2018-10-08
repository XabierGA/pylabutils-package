# Sorting various functions to a criteria that only one of them follows
# template is multisort(guide, data, criteria)

import copy

def multisort(*args):

    def asc(item):
        myitem = [[x, item.index(x)] for x in item]
        myitem.sort()
        return myitem

    def desc(item):
        myitem = [[x, item.index(x)] for x in item]
        myitem.sort(reverse = True)
        return myitem

    def dalt(item):
        temp = [[x, item.index(x)] for x in item]
        myitem = []
        while temp:
            try:
                myitem.append(temp[temp.index(max(temp))])
                del temp[temp.index(max(temp))]
            except(Exception):
                pass
            try:
                myitem.append(temp[temp.index(min(temp))])
                del temp[temp.index(min(temp))]
            except(Exception):
                pass
        return myitem

    sortings = (asc, desc, dalt)

    if len(args) == 3:
        guide, data, criteria = args
        if type(criteria) == str:
            criteria = eval(criteria)
    elif len(args) == 2 and type(args[1]) not in ['function', 'string']:
        guide, data = args
        criteria = asc
    elif not args:
        return sortings
    else:
        raise(ValueError('introduced arguments are invalid'))
        return

    mydict = dict([tuple(x) for x in criteria(guide)])
    findices = list(mydict.values())

    for i in data:
        temp_list = copy.deepcopy(i)
        for j in range(len(i)):
            i[j] = temp_list[findices[j]]

    return data

asc, desc, dalt = multisort()
