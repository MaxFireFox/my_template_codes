def merge(list1, list2):
    fin_list = []
    ind1 = 0
    ind2 = 0
    while ind1 < len(list1) and ind2 < len(list2):
        if list1[ind1] <= list2[ind2]:
            fin_list.append(list1[ind1])
            ind1 += 1
        else:
            fin_list.append(list2[ind2])
            ind2 += 1
    return fin_list + list1[ind1:] + list2[ind2:]


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    else:
        lst1 = merge_sort(lst[:len(lst) // 2])
        lst2 = merge_sort(lst[len(lst) // 2:])
        return merge(lst1, lst2)
