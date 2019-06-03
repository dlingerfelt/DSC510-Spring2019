# Date: 6/3/2019
# Course: DSC 510 - Introduction to Programming
# Desc: Program gets user input on cities in the US and returns weather data
# Usage: Program requests a city or zip code from the user to return weather 
#        forecast. It will return the current forecast as well as two graphs.
#        The first graph displays the temperatures, and the second will display
#        the percipatation (humidity, snow, and rain fall)
import  requests
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import dates

#this is where all the weather magic happens 
class WeatherClass:
    '''
    Weather class is used to pull weater data for zip codes or cities
    '''
    #api_key to request the weather
    api_key = '995b6e1c000e58625548e39c320d57be'
    #base url to request the data through the api
    base_url = 'http://api.openweathermap.org/data/2.5/'
    #initiate the weather class
    def __init__(self):
        self.country = 'us'       
        self._zipCode = 0
        self._city = ''
        self._state = ''
        self._units = 'imperial'
        self._data_weather = {}    #data dictionary for the current weather forecast
        self._data_forecast = {}   #data for the five day forecast
    
    #property decorator and setters for weather class 
    @property
    def zipCode(self):
        return self._zipCode

    @zipCode.setter
    def zipCode(self, _zipCode):
        self._zipCode = _zipCode 
  
    @property
    def city(self):
        return self._city 

    @city.setter
    def city(self, _city):
        self._city = _city
        
    @property
    def state(self):
        return self._state 

    @state.setter
    def state(self, _state):
        self._state = _state
    
    @property
    def city_state(self):
        return '{},{}'.format(self.city,self.state)
    
    @city_state.setter
    def city_state(self,city_state):
        city,state = city_state.split(",")
        #lower to keep url consistent
        self.city = city.lower()
        self.state = state.lower()

    @property
    def units(self):
        return self._units

    @units.setter
    def units(self, _units):
        self._units = _units 

    @property
    def data_weather(self):
        return self._data_weather

    @data_weather.setter
    def data_weather(self, _data_weather):
        self._data_weather = _data_weather
    
    @property
    def data_forecast(self):
        return self._data_forecast

    @data_forecast.setter
    def data_forecast(self, _data_forecast):
        self._data_forecast = _data_forecast
        
    #call weather data by zip code
    def getZipData(self):
        #try, make sure our data works
        try:
            self.getWeatherZip()
            self.getForcastZip()
            #Letting the user know we have connected
            print('Connection was a success!')
            #if data comes back okay, go ahead and print
            self.printWeather()
        except:
            print('Please enter a valid zip code.') #exception passed in the functions above
    
        #call weather data by zip code
    def getCityData(self):
        #try, make sure our data works
        try:
            self.getWeatherCity()
            self.getForcastCity()
            #Letting the user know we have connected
            print('Connection was a success!')
            #if data comes back okay, go ahead and print
            self.printWeather()
        except:
            print('Please enter valid city infromation.') #exception passed in the functions above
    
    
    #call for current weather conditions
    def getWeatherCity(self):
        try:
            #request data from website
            response = requests.get('{0}weather?q={1},{2}&units={3}&appid={4}'.format(self.base_url, self.city_state, self.country, self.units,self.api_key))
            #insert current weather conditions into weather data dictionary
            assert int(response.json()['cod']) < 400
            self.data_weather = response.json()
            self.tranformWeatherData()
            #flag error if issues with request and stop program
        except AssertionError:
            return AssertionError 
        except requests.exceptions.RequestException as e: 
            print(e)
            return e 
                
    #call for 5 day weather conditions          
    def getForcastCity(self):
        try:
            #request data from website
            response = requests.get('{0}forecast?q={1},{2}&units={3}&appid={4}'.format(self.base_url, self.city_state, self.country, self.units,self.api_key))
            #insert 5 day forecast conditions into forecast data dictionary
            assert int(response.json()['cod']) < 400
            self.data_forecast = response.json()
            self.tranformForcastData()
            #flag error if issues with request and stop program
        except AssertionError:
            return AssertionError 
        except requests.exceptions.RequestException as e: 
            print(e)
            return e
     
    
    #call for current weather conditions
    def getWeatherZip(self):
        try:
            #request data from website
            response = requests.get('{0}weather?zip={1},{2}&units={3}&appid={4}'.format(self.base_url, self.zipCode, self.country, self.units,self.api_key))
            #insert current weather conditions into weather data dictionary
            assert int(response.json()['cod']) < 400
            self.data_weather = response.json()
            self.tranformWeatherData()
            #flag error if issues with request and stop program
        except AssertionError:
            return AssertionError 
        except requests.exceptions.RequestException as e: 
            print(e)
            return e 
                
    #call for 5 day weather conditions          
    def getForcastZip(self):
        try:
            #request data from website
            response = requests.get('{0}forecast?zip={1},{2}&units={3}&appid={4}'.format(self.base_url, self.zipCode, self.country, self.units,self.api_key))
             #insert 5 day forecast conditions into forecast data dictionary
            assert int(response.json()['cod']) < 400
            self.data_forecast = response.json()
            self.tranformForcastData()
            #flag error if issues with request and stop program
        except AssertionError:
            return AssertionError 
        except requests.exceptions.RequestException as e: 
            print(e)
            return e  
    
    @staticmethod
    def degreesToCardinal(deg):
        direction = { "N":[337.5, 22.5], "NE":[22.5, 67.5], "E":[67.5, 112.5], "SE":[112.5, 157.5], "S":[157.5, 202.5], "SW":[202.5, 247.5], "W":[247.5, 292.5], "NW":[292.5, 337.5]};
        for key,val in direction.items():
            if deg >= val[0] and deg <val[1]:
                return key
                
    def tranformWeatherData(self):
        #timezone and date used to display current time in place of request
        timezone = self.data_weather['timezone']
        current_date = datetime.utcfromtimestamp(self.data_weather['dt'] +  self.data_weather['timezone'] )
        #get the weather description
        desc = self.data_weather['weather'][0]['description']
        #current temp
        temp = self.data_weather['main']['temp']
        #current humidity
        humidity = self.data_weather['main']['humidity']
        #get sunrise and sunset
        sunrise = current_date = datetime.utcfromtimestamp(self.data_weather['sys']['sunrise'] + timezone)
        sunset = current_date = datetime.utcfromtimestamp(self.data_weather['sys']['sunset'] + timezone)
        #try used if null will set values to 0
        try:
            rain = '{} mm'.format(self.data_weather['rain']['1h'])
        except:
            rain = '0'
        try:
            snow = '{} mm'.format(self.data_weather['snow']['1h'])
        except:
            snow = '0'
        try:
            wind = '{} mph {}'.format(self.data_weather['wind']['speed'], self.degreesToCardinal(self.data_weather['wind']['deg']))
        except:
            wind = '0 mph'
        #update data_weather, to better access what we need
        self.data_weather = {'current_date': current_date, 'desc':desc, 'temp':temp, 'humidity': humidity, 'rain':rain, 'snow':snow, 'wind':wind, 'sunrise':sunrise,'sunset':sunset }
       
    
    #this is used to transform forecast dates
    def tranformForcastData(self):
        #constructing lists
        dates = []
        temps = []
        humidity = []
        clouds = []
        rain = []
        snow = []
        #timezone and date used to display current time in place of request
        timezone = self.data_forecast['city']['timezone']
        for i in self.data_forecast['list']:
            #date and time used to plot graph 
            dates.append(datetime.utcfromtimestamp(i['dt'] + timezone))
            #storing temperatures, humidity, clouds
            temps.append(i['main']['temp'])
            humidity.append(i['main']['humidity'])
            clouds.append( i['clouds']['all'])
            #try used to make sure we capture a data point for each list so it matches dates, set to zero if it doesn't exist
            try:
                #converting to inches, since I ran out of time to ask user for imperial vs metric
                rain.append(i['rain']['3h'] * 0.0393701)
            except:
                rain.append(0)
            try:
                #converting to inches, since I ran out of time to ask user for imperial vs metric
                snow.append(i['snow']['3h'] * 0.0393701)
            except:
                snow.append(0)
        #update data_forecast for ploting graphs
        self.data_forecast = { 'dates': dates, 'temps':temps, 'humidity': humidity,'rain': rain,'snow': snow  }
    
    #used to pull the minimum time from dates 
    @staticmethod
    def getMinHour(inList):
        #construct list
        hour =[]
        #try used in case it is called and no data sent or bad data is sent
        try:
            for i in inList:
                #insert hour values to see the min
                hour.append(i.strftime("%H"))
            return int(min(hour))
        except:
            #inform user data is bad
            print('error: bad dates entered from list')
            #used to flag an error that there is no data
            return AssertionError 
            
    #print the 5 day forecast
    def printForecastGraph(self):
        #use x and y values to make it simpler to read
        x = self.data_forecast['dates']
        y = self.data_forecast['temps']
        #this is used so that we can draw line for when the dates start and end
        min_x = self.getMinHour(x)

        #setup graph
        fig6, ax = plt.subplots()
        #naming of the graph and axis
        ax.set_title("5 Day Forecast")
        ax.set_xlabel("Day")
        ax.set_ylabel("Temperature")
        #setup graph to plo
        ax.plot(x, y)
        #start both axis at 0
        ax.margins(0)
        #create vertical line at midnight for each graph
        for i in x:
            #compare hour to min
            if int(i.strftime("%H")) == int(min_x):
                ax.axvline(i,color = 'g')
        #set the Mon, Tues,... at the 12 pm position
        ax.xaxis.set_major_locator(dates.HourLocator(byhour = 12))
        #format dates to Mon, Tues, Wed, etc
        ax.xaxis.set_major_formatter(dates.DateFormatter("%a"))
        #set grid lines 
        ax.grid()
        plt.show()
        
        
        
    #print the 5 day forecast
    def printHumidity(self):
        #use x and y values to make it simpler to read
        x = self.data_forecast['dates']
        y = self.data_forecast['humidity']
        #this is used so that we can draw line for when the dates start and end
        min_x = self.getMinHour(x)

        #setup graph
        fig6, ax = plt.subplots()
        #naming of the graph and axis
        ax.set_title("5 Day Forecast: Humidity")
        ax.set_xlabel("Day")
        ax.set_ylabel("% Humidity")
        #setup graph to plo
        ax.plot(x, y, color = 'r')
        #start both axis at 0
        ax.margins(0)
        #create vertical line at midnight for each graph
        for i in x:
            #compare hour to min
            if int(i.strftime("%H")) == int(min_x):
                ax.axvline(i,color = 'g')
        #set the Mon, Tues,... at the 12 pm position
        ax.xaxis.set_major_locator(dates.HourLocator(byhour = 12))
        #format dates to Mon, Tues, Wed, etc
        ax.xaxis.set_major_formatter(dates.DateFormatter("%a"))
        #set grid lines 
        ax.grid()
        plt.show()
        
    #print the 5 day forecast
    def printPercipation(self):
        #use x and y values to make it simpler to read
        x = self.data_forecast['dates']
        y_rain = self.data_forecast['rain']
        y_snow = self.data_forecast['snow']
        #this is used so that we can draw line for when the dates start and end
        min_x = self.getMinHour(x)

        #setup graph
        fig6, ax = plt.subplots()
        #naming of the graph and axis
        ax.set_title("5 Day Forecast:Percipatation")
        ax.set_xlabel("Day")
        ax.set_ylabel("Percipatation (inches)")
        #setup graph to plot
        ax.plot(x, y_rain, color='blue', label = 'Rain')
        ax.plot(x, y_snow, color='yellow', label = 'Snow')
        ax.legend()

        #start both axis at 0
        ax.margins(0)
        #create vertical line at midnight for each graph
        for i in x:
            #compare hour to min
            if int(i.strftime("%H")) == int(min_x):
                ax.axvline(i,color = 'g')
        #set the Mon, Tues,... at the 12 pm position
        ax.xaxis.set_major_locator(dates.HourLocator(byhour = 12))
        #format dates to Mon, Tues, Wed, etc
        ax.xaxis.set_major_formatter(dates.DateFormatter("%a"))
        #set grid lines 
        ax.grid()
        plt.show()
        
        
    #used to display the weather for the user
    def printWeather(self):
        #print current conditions
        print('\n\nCurrent weather for {0}:\n{1}, temperature: {2} F\nWind: {3} \nHumidity: {4} % \nRain: {5} mm\nSnow: {6} mm\nSunrise: {7}\nSunset: {8}'.format(self.data_weather['current_date'].strftime("%x"),self.data_weather['desc'],self.data_weather['temp'],self.data_weather['wind'] ,self.data_weather['humidity'],self.data_weather['rain'],self.data_weather['snow'],self.data_weather['sunrise'].strftime("%I:%M:%S %p"),self.data_weather['sunset'].strftime("%I:%M:%S %p")))
        #print 5 day forecasts
        self.printForecastGraph()
        self.printHumidity()
        self.printPercipation()

def main():
    #used to keep the loop going until marked false
    isContinue = True
    #user prompts to keep the user engaged in the program
    promptBegin = 'Welcome,\nThis program allows you to enter a zip code or a city and state.\nWhen you enter the data it will return the current weather conditions and a 5 day forecast.\nFeel free to enter as many cities as you would like. All weather is based out of the US.'
    promptFormatting = '(Formatting: City- City, State = Atlanta, GA OR zip = 83201)'
    promptContinue = '\nTo continue, enter a zip code or city and state.{}.'.format(promptFormatting)
    promptAssert = '\nThe zip code that you entered must be a number greater than 0.'
    promptError = '\nOops, somethings off, make sure to include a comma in between city and state.'
    promptExit = '\nThank you for using this software, please come again soon!' 
    print(promptBegin)
    #continue to enter data until the user hits'q'
    while(isContinue):
        user_input = input(promptContinue)
        weather = WeatherClass()
        try:
            if user_input.lower() == 'q':
                print(promptExit)
                isContinue = False
            else:
                if ',' in user_input:
                    weather.city_state = user_input
                    weather.getCityData()
                    
                else:
                    user_input = int(user_input)
                    assert user_input > 0
                    weather.zipCode = user_input
                    weather.getZipData()
                    
                
        except AssertionError:
            print(promptAssert)
        except:
            print(promptError)            
        
    
                
if __name__ == "__main__":
    main()

 




