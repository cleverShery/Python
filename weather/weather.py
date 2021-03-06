from tkinter import *
import requests
import json

root = Tk()
root.title("Air Quality")
root.geometry("600x100")

# Create zipcode lookup function 
def zipLookup():

    try:
        api_request = requests.get(f"https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code.get()}&distance=5&API_KEY=BAFEDAAE-E484-4206-9BB3-3D5A96F7C585")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == 'Good':
            weather_color = '#00E400'
        elif category == 'Moderate':
            weather_color = '#ffff00'
        elif category == 'Unhealthy for Sensitive Groups':
            weather_color = '#ff7e00'
        elif category == 'Unhealthy':
            weather_color = '#ff0000'
        elif category == 'Very Unhealthy':
            weather_color = '#8F3F97'
        elif category == 'Hazardous':
            weather_color = '#7E0023'

        root.configure(background=weather_color)

        my_label = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Alternate Gothic", 20), background=weather_color)
        my_label.grid(row=1, column=0, columnspan=2)
    except Exception as e:
        api = "Error..."
        my_label = Label(root, text=api)
        my_label.grid(row=1, column=0, columnspan=2)

zip_code = Entry(root)
zip_code.grid(row=0, column=0, sticky=E+W+N+S)

zip_btn = Button(root, text="Lookup Zipcode", command=zipLookup)
zip_btn.grid(row=0, column=1, sticky=E+W+N+S)

root.mainloop()