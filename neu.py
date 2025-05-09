import requests

BASE_URL = "https://media.ccc.de/public/"
LIVE_URL = "https://streaming.media.ccc.de/streams/v2.json"
RELIVE_URL = "https://cdn.c3voc.de/relive/index.json"


class FetchError(Exception):
    pass


def fetch_data(endpoint):
    try:
        response = requests.get(BASE_URL + endpoint)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Fehler beim Abrufen von Daten: {e}")
        raise FetchError(e)


def fetch_recordings(event):
    try:
        # Teste alternative Endpunkte
        data = fetch_data(f"conferences/{event}/events")
        return data.get("recordings", [])
    except FetchError as e:
        print(f"Fehler: Die Event-Daten für '{event}' konnten nicht abgerufen werden.")
        return []


def list_conferences():
    try:
        conferences = fetch_data("conferences")
        print("### Verfügbare Konferenzen ###")
        for conf in conferences.get("conferences", []):
            print(
                f"Konferenz: {conf.get('title', 'Unbekannt')} (Slug: {conf.get('slug', 'Kein Slug')})"
            )
    except FetchError:
        print("Fehler: Konferenzdaten konnten nicht abgerufen werden.")


def list_recordings_for_conference(slug):
    print(f"Aufnahmen für Konferenz '{slug}' werden abgerufen...")
    recordings = fetch_recordings(slug)
    if not recordings:
        print(
            f"Keine Aufnahmen für die Konferenz '{slug}' gefunden. Bitte überprüfen Sie den Slug."
        )
        return
    for rec in recordings:
        print(
            f"Titel: {rec.get('recording_url', 'Keine URL')}, Typ: {rec.get('mime_type', 'Unbekannt')}"
        )


def main():
    list_conferences()

    print("\n### Aufnahmen für eine Konferenz ###")
    slug = input("Bitte geben Sie den Slug einer Konferenz ein: ")
    list_recordings_for_conference(slug)


if __name__ == "__main__":
    main()
