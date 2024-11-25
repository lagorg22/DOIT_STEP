# შექმენით async ფუნქცია write_to_file, რომელიც ატრიბუტის სახით იღებს ფაილის სახელს და ჩასაწერი სტრინგის
# მნიშვნელობას.asyncio.sleep-ის გამოყენებით, მცირე დაყოვნების შემდეგ, ჩაწერეთ სტრინგის მნიშვნელობა ფაილში.
# დაბეჭდეთ თასქის დაწყება და დასრულება. გამოიყენეთ asyncio.gather მინიმუმ 3 სხვადასხვა ფაილში ერთდროულად ჩასაწერად.

import asyncio

async def write_to_file(f_path: str, txt: str):
    print(f'writing {txt} into {f_path}')
    await asyncio.sleep(2)
    with open(f_path, 'w') as f:
        f.write(txt)
    print(f'writing in {f_path} finished')

async def main():
    file_paths = ['f1.txt', 'f2.txt', 'f3.txt']
    txts = ['1111111111111111111111', '222222222222222222222', '333333333333333333333333333']
    couples = zip(file_paths, txts)
    tasks = [write_to_file(f_path, txt) for f_path, txt in couples]
    await asyncio.gather(*tasks)

asyncio.run(main())

