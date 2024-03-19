from api_key import APIkey
import requests


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    no_values = 8 * forecast_days
    filtered_data = filtered_data[:no_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Mumbai", forecast_days=2))
    f_data = get_data(place="Mumbai", forecast_days=2)
    print([dict["dt_txt"] for dict in f_data])
    print([type(dict) for dict in f_data])

