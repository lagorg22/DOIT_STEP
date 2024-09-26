import random


rand_num_list = [random.randint(0, 100) for _ in range(20)]


odd_nums = [num for num in rand_num_list if num % 2]

print(f'Minimun: {min(odd_nums)}\n'
      f'Maximum: {max(odd_nums)}')