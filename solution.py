def countDigits(num):
    """
    :type num: int
    :rtype: int
    """
    count = 0
    for i in str(num):
        if int(i) == 0:
            None
        elif num % int(i) == 0:
            count += 1
    return count
