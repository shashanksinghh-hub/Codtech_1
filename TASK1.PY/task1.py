import requests 
import matplotlib.pyplot as plt
city_name= 'Bhopal'
API_key ='f7121f2976f44fcdc736e845b00f1eeb'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('Weather is', data['weather'][0]['description'])
    print('current Temperature is ', data['main']['temp'])
    print('Current Temperature feels like is',data['main']['feels_like'])
    print('Humidity is', data['main']['humidity'])
    print('Wind Speed is', data['wind']['speed'])

    # Adding matplotlib visualization
    # Plotting temperature data
    temperatures = [data['main']['temp'], data['main']['feels_like'], data['main']['temp_min'], data['main']['temp_max']]
    labels = ['Current', 'Feels Like', 'Min', 'Max']
    
    plt.figure(figsize=(8, 5))
    plt.bar(labels, temperatures, color=['blue', 'orange', 'green', 'red'])
    plt.ylabel('Temperature (°C)')
    plt.title(f'Temperature Data for {city_name}')
    plt.ylim(min(temperatures) - 5, max(temperatures) + 5)  # Adjust y-axis for better view
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
    # Optional: Plot humidity and pressure as a simple bar chart
    other_data = [data['main']['humidity'], data['main']['pressure']]
    other_labels = ['Humidity (%)', 'Pressure (hPa)']
    
    plt.figure(figsize=(6, 4))
    plt.bar(other_labels, other_data, color=['purple', 'brown'])
    plt.title(f'Humidity and Pressure for {city_name}')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")
    print(response.text)

