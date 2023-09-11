# weather_assignment

Created by Zachary Debski
Created on 9/11/2023

##purpose:
connect to openweathermapi.org and return weather data by zipcode

###weather_api.py:
Create an api endpoint to connect to openweathermap.org/api

path paramaters =  zipcode
query paramaters = zipcode, units, apikey

zipcode = zipcode of where you want to see weather data

units = the measurement you want to return the temperature data
  (imperial = fareinheight)
  
apikey = personal token used to connect to openmap api 




###diagram.py:
package that consumes the api and creates a graph of the JSON response
