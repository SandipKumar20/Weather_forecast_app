from api_key import APIkey
import requests


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    no_values = 8 * forecast_days
    filtered_data = filtered_data[:no_values]
    match kind:
        case "Temperature":
            filtered_data = [dict["main"]["temp"] for dict in filtered_data]
        case "Sky":
            filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=2, kind="Temperature"))
