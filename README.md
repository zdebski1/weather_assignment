# Weather_Assignment:

- Created by Zachary Debski
- Created on 9/11/2023

## Purpose:
  connect to openweathermapi.org and return weather data by zipcode

### weather_api.py:
Creates an api endpoint to connect to openweathermap.org/api

endpoint example: http://api.openweathermap.org/data/2.5/weather?zip={zip_code}&units={units}&appid={api_key}

  - API Paramaters:
    - path paramaters =  zipcode
    - query paramaters = zipcode, units, apikey

  - zipcode:
    - zipcode of where you want to see weather data
    - value must be: 5 digits long

  - units:
    -  Measurement you want the temperature to return as 
    - values must be: imperial, standard, or metric
  
  - apikey:
    - personal token used to connect to openmap api, this can be obtained after creating an account from openweathermap.org/api




### diagram.py:
package that consumes the api and creates a graph of the JSON response

package will also return a python cli where it will ask for user zipcode, type of unit, and apikey
