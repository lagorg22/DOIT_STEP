tuple1 = (1,2,3,4,5,6)
tuple2 = (4,5,5,6,6,7)

combined_tuple = tuple(set(tuple1 + tuple2))

duplicated_values = list(set(tuple1).intersection(set(tuple2)))

print(f'Combined Tuple with unique values: {combined_tuple}\n'
      f'Tuple with duplicated values: {duplicated_values}')