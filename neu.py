import requests

other = "https://media.ccc.de/public/recordings/"
url = "https://media.ccc.de/public/conferences/"
r = requests.get(url=url)
myjson = r.json()
conferences = myjson["conferences"]
for i in range(len(conferences)):
    print(f"Acronym {conferences[i]["acronym"]} - {conferences[i]["acronym"]}")
