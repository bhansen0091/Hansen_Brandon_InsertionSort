
test_list = [5,9,8,6,7,3,4,2,1,0]

def insertion(p_list):
    for i in range(1,len(p_list)):
        insert = i
        while p_list[insert-1] > p_list[insert] and insert > 0:
            p_list[insert-1], p_list[insert] = p_list[insert], p_list[insert-1]
            insert -= 1
    return p_list

print(insertion(test_list))
