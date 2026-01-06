def ft_count_harvest_recursive(limit=None, where=None):
    if limit is None:
            limit = int(input("Days until harvest: "))
    where = where or 0
    if where < limit:
        where += 1
        print("Day", (where))
        ft_count_harvest_recursive(limit, where)
    else:
        print("Harvest time!")
