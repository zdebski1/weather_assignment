import asyncio
from fastapi import FastAPI, HTTPException
import weather_api
from pydantic import BaseModel, Field 

## figure out how to do mermaid chart ## 

## https://mermaid.js.org/intro/ 




class weather_data(BaseModel): # create a class using pydantics to insure that the zipcode can only be 5 digits long
    zip_code: str = Field(max_length=5, min_length=5)
    units: str
    api_key: str



async def main():
    zip_code = input('Zipcode: ')
    units = input('Unit of measurement: ')
    api_key = '2cad35927d4cc9b4f8b0d5077090f6dd'  #input('personal token: ')

    data = weather_data(zip_code=zip_code, units=units, api_key=api_key)
    temperature = await weather_api.get_weather_by_zipcode(data.zip_code, data.units, data.api_key)
    
    print(temperature)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
