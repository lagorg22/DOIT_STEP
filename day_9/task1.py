int_list = [10,20,30,40]

def fun(num):
    global int_list
    int_list.append(num)

fun(11)
print(int_list)