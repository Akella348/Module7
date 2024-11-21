import asyncio
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for ball in range(1,6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял шар №{ball}')
    print(f'Силач {name} закончил соревнования')
async def start_tournament():
    strongmans = [('Pasha',3),('Sasha',4),('Hercules',5)]
    tasks = [start_strongman(name, power) for name, power in strongmans]
    await asyncio.gather(*tasks)
asyncio.run(start_tournament())