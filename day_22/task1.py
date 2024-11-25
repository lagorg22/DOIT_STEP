# დაწერეთ ორი ასინქრონული ფუნქცია, ერთ-ერთი დააყოვნეთ 2 წამი, მეორე 5 წამი, დაბეჭდეთ მათი
# დაწყება და დასრულება, თასქები შექმენით ცალ-ცალკე და გაუშვით.

import asyncio

async def task1():
    print('task1 started.')
    await asyncio.sleep(2)
    print('task1 done.')

async def task2():
    print('task2 started.')
    await asyncio.sleep(5)
    print('task2 done.')

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())