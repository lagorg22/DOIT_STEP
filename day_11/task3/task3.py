with open('f1.txt', 'w') as f:
    f.write('kfjflkdsajflksfnskdfdsflkdsf\njkfhdskjfhkjsfds')

with open('f2.txt', 'w') as f:
    f.write('kjdlkajdiuiahdu213j23jhkj21321\n3213432j4h32hkjhkjfds\nhrjkhar\n')

with open('f1.txt', 'r') as f:
    f1_txt = f.read()

with open('f2.txt', 'r') as f:
    f2_txt = f.read()


with open('res.txt', 'w') as f:
    f.write(f'{f1_txt}\n{f2_txt}')


