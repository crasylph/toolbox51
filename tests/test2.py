import asyncio

async def test():
    print("start")
    await asyncio.sleep(1)
    print("end")
    
async def main():
    print(11111111)
    task1 = asyncio.create_task(test())
    task2 = asyncio.create_task(test())
    print(2222222)
    await task1
    await task2
    print(33333333)
    
if __name__ == "__main__":
    asyncio.run(main())