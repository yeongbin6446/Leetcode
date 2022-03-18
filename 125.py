def is_palindrome(s : str) -> bool:
    lst = []
    for i in s:
        if i.isalnum():
            lst.append(i.lower())

    lst2 = lst.copy()
    lst.reverse()
    return lst == lst2

print(is_palindrome("A man, a plan, a canal : Panama"))