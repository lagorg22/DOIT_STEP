
my_list = [43, '22', 12, 66, 210, ["hi"]]

print(f'index of element 210: {my_list.index(210)}')

my_list[-1][0] += ' hello'

my_list.pop(1)
print(f'my_list after deleting second element: {my_list}')

my_list_2 = my_list
my_list_2.clear()
print(f'both of the lists get erased: \n'
      f'my_list: {my_list}\n'
      f'my_list_2: {my_list_2}')
