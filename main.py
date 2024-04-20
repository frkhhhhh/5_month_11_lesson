

import time
import asyncio
import httpx

start=time.perf_counter()
urls=[
    "https://jsonplaceholder.typicode.com/users/1",
    "https://jsonplaceholder.typicode.com/users/2",
    "https://jsonplaceholder.typicode.com/users/3",
    "https://jsonplaceholder.typicode.com/users/4",
    "https://jsonplaceholder.typicode.com/users/5"
]

async def fetch_all(url):
    async with httpx.AsyncClient() as client:
        rsp= await client.get(url)

        return rsp.json()
async def all():
    mdl=[fetch_all(url) for url in urls]
    res=await asyncio.gather(*mdl)

    for resss in res:
        print(resss)    
asyncio.run(all())
end=time.perf_counter()
print(f"Processed {end-start}")


    
