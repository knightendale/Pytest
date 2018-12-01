num = input('Enter an integer: ')


def sqaure(num):
    if not num.isdigit():
        return 'Invalid Entry'
    num = int(num)
    return num * num


print(num, 'Squared is: ', sqaure(num))
