strings = ['ab', 'sab', 'dfabfd']


def x(strings):
    min_st = ''
    count = 0
    for i in strings:
        if count > 0 and len(min_st) > len(i):
            min_st = i
        elif count == 0:
            min_st = i
            count += 1

    for i in strings:
        for j in range(len(min_st)):
            if min_st[j] == i[j]:
                print(i)
            else:
                for s in range(len(i)):
                    if min_st[j] == i[s]:


x(strings)
