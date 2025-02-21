import requests
from bs4 import BeautifulSoup

URL = "https://www.anilibria.tv/pages/schedule.php"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def get_html(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None


def get_schedule(html):
    soup = BeautifulSoup(html, "html.parser")

    schedule_items = soup.find_all("div", class_="schedule-series")

    schedule_list = []
    for item in schedule_items:
        title_tag = item.find("div", class_="schedule-series-title")
        if title_tag:
            title = title_tag.get_text(strip=True)
            schedule_list.append({"title": title})

    return schedule_list


def parsing_anilibria():
    html = get_html(URL)
    if html:
        return get_schedule(html)
    else:
        print("Ошибка при получении страницы")
        return []


if __name__ == "__main__":
    schedule = parsing_anilibria()
    for anime in schedule:
        print(anime)
