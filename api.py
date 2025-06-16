import requests

headers = {
    "X-RapidAPI-Key": "92236ffd02msh9b1b336546871abp17abffjsn7190dfcf8704",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

def get_standings():
    url = "https://api-football-v1.p.rapidapi.com/v3/standings"

    querystring = {
        "season": "2023",
        "league": "39"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()['response'][0]['league']['standings'][0]
