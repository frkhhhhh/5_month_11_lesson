# import asyncio
# import httpx


# urls=[
#     "https://jsonplaceholder.typicode.com/users/1",
#     "https://jsonplaceholder.typicode.com/users/2",
#     "https://jsonplaceholder.typicode.com/users/3",
#     "https://jsonplaceholder.typicode.com/users/4",
#     "https://jsonplaceholder.typicode.com/users/5"
# ]

# async def fetch_data(url):
#     async with httpx.AsyncClient() as client:
#         rsp= await client.get(url)
#         return rsp.json()
    
# async def main():
#     tm=[fetch_data(url) for url in urls]
#     res=await asyncio.gather(*tm)
#     for ress in res:
#         print(ress)


# asyncio.run(main())   
import asyncio
import httpx
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


    