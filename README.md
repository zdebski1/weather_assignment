# weather_assignment

Created by Zachary Debski
Created on 9/11/2023

## purpose:
  connect to openweathermapi.org and return weather data by zipcode

### weather_api.py:
  Creates an api endpoint to connect to openweathermap.org/api

  API Paramaters:
    path paramaters =  zipcode
    query paramaters = zipcode, units, apikey

  zipcode = zipcode of where you want to see weather data
  (value must be: 5 digits long)

  units = the measurement you want to return the temperature data
  (values must be: imperial, standard, or metric)
  
  apikey = personal token used to connect to openmap api




### diagram.py:
package that consumes the api and creates a graph of the JSON response
package will also return a python cli where it will ask for user zipcode, type of unit, and apikey
