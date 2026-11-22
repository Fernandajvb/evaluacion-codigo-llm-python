def find_tuples(test_list, k):
    return [tup for tup in test_list if all(ele % k == 0 for ele in tup)]
