import requests
from bs4 import BeautifulSoup

def parse():
    url = "https://www.imdb.com/chart/top/"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    print("Status Code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    movies = soup.select("td.titleColumn")
    ratings = soup.select("td.imdbRating strong")

    top_250 = {}

    for i in range(len(movies)):
        title = movies[i].get_text(strip=True).split('.', 1)[-1].strip()
        rating = ratings[i].text.strip()
        top_250[title] = rating

    # Сохраняем в текстовый файл
    with open("top_250.txt", "w", encoding="utf-8") as file:
        for title, rating in top_250.items():
            file.write(f"{title}: {rating}\n")

    print("Результат сохранён в файл top_250.txt")

if __name__ == '__main__':
    parse()
