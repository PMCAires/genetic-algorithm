a = [1, 2, 3, 4, 5, 6]

def is_member_of (ls, n):
    for i in ls:
        if i == n:
            return True
    return False


def is_member (ls, n):
    if not (ls):
        return False
    elif ls[0:] == n:
        return True
    else:
        return is_member(ls[1:], n)

print (is_member ([1,2,3,4], 12))

