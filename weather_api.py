'''
for feirnheight, use units = imperial, per the documentation: https://openweathermap.org/api/one-call-3#data

Temperature is available in Fahrenheit, Celsius and Kelvin units.
Wind speed is available in miles/hour and meter/sec.

For temperature in Fahrenheit and wind speed in miles/hour, use units=imperial
For temperature in Celsius and wind speed in meter/sec, use units=metric
Temperature in Kelvin and wind speed in meter/sec is used by default, so there is no need to use the units parameter in the API call if you want this
 
'''


from fastapi import APIRouter, HTTPException, status
import httpx
from pydantic import BaseModel, Field

router = APIRouter()

# class weather_data(BaseModel):
#     zipcode: str = Field(min_length=5, max_length=5)
#     units: str
#     api_key: str


@router.get('/zipcode/{zipcode}', status_code=status.HTTP_200_OK)
async def get_weather_by_zipcode(zip_code: str, units: str, api_key: str):

    if units not in ["imperial", "metric", "standard"]:
        raise HTTPException(status_code=400, detail='Please use imperial, metric, or standard')

    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_code}&units={units}&appid={api_key}"
    try:
        async with httpx.AsyncClient() as client:
            openmap_response = await client.get(url)
            openmap_response.raise_for_status()

            weather_data = openmap_response.json()
            temp = weather_data.get("main", {}).get("temp")

            if temp is not None:
                return {f"The temperature in {units} units for {zip_code} is:": temp}
            else:
                raise HTTPException(status_code=404, detail='Source not found')

    except:
        HTTPException(status_code=500, detail='Cannot connect to server')
