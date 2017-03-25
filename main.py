
import pyowm
from pushbullet import Pushbullet

pb = Pushbullet('Your_pushbulled_api_key')


temp = 0.0
owm = pyowm.OWM('Your_open_weathermap_api_key')  # You MUST provide a valid API key

observation = owm.weather_at_place('Kennewick,US')
w = observation.get_weather()
#print()                      
# Weather details
stats = w.get_status
print stats + 1
print w.get_wind                
hum =  w.get_humidity()             
temp = w.get_temperature('celsius')  
#temp = temp - 32 * 5 / 9
z = float(temp['temp'])
#stats = stats['status']

def convertandsend(x):
        x = x * 1.8 + 32
        x = round(x, 0)
        print x
        z = x
        push = pb.push_note("Status", "The current temp is %s Degrees, with %s percent  humidity it is currently %s" %(z,hum,stats))




convertandsend(z)

