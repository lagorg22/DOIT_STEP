# დაწერეთ ასინქრონული ფუნქცია, დააბრუნებს ატრიბუტად გადაწოდებული რიცხვის კვადრატს,
# იმ შემთხვევაში თუ ეს რიცხვი არის ლუწი, ამის შესამოწმებლად დაწერეთ მეორე ასინქრონული ფუნქცია.
# შესამოწმებლად შექმენით რამდენიმე თასქი, გამოიყენეთ gather მეთოდი

import asyncio

async def check(num: int):
    return not num % 2

async def square(num: int):
    is_even = await check(num)
    if is_even:
        print(num * num)
    else:
        print('The num is odd.')

async def main():
    tasks = [square(i) for i in range(10)]
    await asyncio.gather(*tasks)

asyncio.run(main())