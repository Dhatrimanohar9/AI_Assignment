def get_aqi(pm25):
    if pm25 <= 50:
        return "Good"
    elif pm25 <= 100:
        return "Moderate"
    elif pm25 <= 150:
        return "Unhealthy for Sensitive Groups"
    elif pm25 <= 200:
        return "Unhealthy"
    else:
        return "Very Unhealthy"


def simple_reflex_agent(sensor_value):
    return get_aqi(sensor_value)


pm25 = int(input("Enter PM2.5 value: "))
aqi = simple_reflex_agent(pm25)

print("AQI Level:", aqi)
