def square_digits(num):
    # Your code here
    string_num = str(num)
    a_list_of_num = []
    for char in string_num:
        cast_char = int(char)
        a_list_of_num.append(int(char) * int(char))

    result = ""
    for item in a_list_of_num:
        result += str(item)

    print(int(result))
    print(type(result))
    return int(result)


square_digits(9119)

# from code wars
# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)
