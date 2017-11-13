from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

apikey = "OA9RkoKdJITqRlOa59bxhPLEOGiefRXx"
locationKey = "349727"

@app.route('/')
def root():
    u = urllib2.urlopen("http://dataservice.accuweather.com/forecasts/v1/daily/1day/" + locationKey + "?apikey=" + apikey)
    response = u.read()
    data = json.loads(response)

    temp = data["DailyForecasts"][0]
    
    date = temp["Date"][:10]
    minimum = temp["Temperature"]["Minimum"]["Value"]
    maximum = temp["Temperature"]["Maximum"]["Value"]
    unit = temp["Temperature"]["Minimum"]["Unit"]
    day = temp["Day"]["IconPhrase"]
    night = temp["Night"]["IconPhrase"]
    link = temp["Link"]

    return render_template('home.html', date = date, minimum = minimum, maximum = maximum, unit = unit, day = day, night = night, link = link)

if __name__ == '__main__':
    app.debug = True
    app.run() 
