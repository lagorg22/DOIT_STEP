# დაწერეთ ასინქრონული ფუნქცია, რომელიც რენდომად არჩეული დროით დააყოვნებს და დაბეჭდავს რიცხვებს 1-დან 10-მდე

import asyncio
import random

async def foo():
    for i in range(1, 11):
        delay = random.randint(1, 3)
        await asyncio.sleep(delay)
        print(i)

async def main():
    await foo()

asyncio.run(main())