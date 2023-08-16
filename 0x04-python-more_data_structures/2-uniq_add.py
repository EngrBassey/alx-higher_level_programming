def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    count = 0
    for i in range(len(new_list)):
        count += new_list[i]
    return (count)
