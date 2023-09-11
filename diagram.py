import asyncio
from fastapi import FastAPI, HTTPException
import weather_api
from pydantic import BaseModel, Field 

## figure out how to do mermaid chart ## 

## https://mermaid.js.org/intro/ 




# app = FastAPI()
# app.include_router(weather_api.router)


async def main():

        zip_code = input('Zipcode: ')
        units = input('Unit of measurement: ')
        api_key = input('personal token: ')

        temperature = await weather_api.get_weather_by_zipcode(zip_code, units, api_key)
        print(temperature)


if __name__ == "__main__":
    # Create a loop and run until complete
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())