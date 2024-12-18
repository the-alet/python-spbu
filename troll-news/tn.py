import difflib
import json
import requests
from difflib import SequenceMatcher
from bs4 import BeautifulSoup
from typing import List
import os


def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

class News:
    def __init__(self, title: str, annotation: str, full_text: str, url: str):
        self.title = title
        self.annotation = annotation
        self.full_text = full_text
        self.url = url

    def __repr__(self):
        return f"News(title={self.title}, url={self.url})"

class Joke:
    def __init__(self, text: str):
        self.text = text

    def __repr__(self):
        return f"Joke(text={self.text[:30]}...)"

class RBCNewsGrabber:
    def __init__(self, rss_url: str):
        self.rss_url = rss_url

    def fetch_news(self) -> List[News]:
        response = requests.get(self.rss_url)
        soup = BeautifulSoup(response.content, 'xml')
        news_items = soup.find_all('item')
        news = []

        for item in news_items:
            title = item.title.text
            link = item.link.text
            description = item.description.text
            news.append(News(title, description, description, link))

        return news

class JokesGrabber:
    def __init__(self, cache_file: str):
        self.cache_file = cache_file

    def fetch_jokes(self, url: str) -> List[Joke]:
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                jokes = json.load(f)
            return [Joke(text) for text in jokes]

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        jokes = [joke.text.strip() for joke in soup.find_all('div', class_='text')]

        with open(self.cache_file, 'w', encoding='utf-8') as f:
            json.dump(jokes, f, ensure_ascii=False, indent=2)

        return [Joke(text) for text in jokes]

class TrollFactory:
    def __init__(self, jokes: List[Joke]):
        self.jokes = jokes



    def find_similar_joke(self, news: list[News]) -> list[(News, Joke, float)]:
        result = []
        for string1 in news:
            best_match = None
            highest_similarity = 0.0

            for string2 in self.jokes:
                # Оцениваем схожесть строк
                similarity = SequenceMatcher(None, string1.full_text, string2.text).ratio()
                if similarity > highest_similarity:
                    highest_similarity = similarity
                    best_match = string2

            # Добавляем в результат кортеж из строки, её лучшего совпадения и коэффициента схожести
            result.append((string1, best_match, highest_similarity))

            # Сортируем по убыванию коэффициента схожести
        result.sort(key=lambda x: x[2], reverse=True)

        return result


    def generate_troll_news(self, news_list: List[News]) -> List[News]:
        news = []
        tns = self.find_similar_joke(news_list)
        for n in tns:
            n[0].full_text += f"\nАнекдот: {n[1].text}\nКоэффициент схожести: {n[2]}\n"
            news.append(n[0])
        return news

class NewsSaver:
    @staticmethod
    def save_to_file(news_list: List[News], file_path: str):
        with open(file_path, 'w', encoding='utf-8') as f:
            for news in news_list:
                f.write(f"{news.title}\n")
                f.write(f"{news.full_text}\n")
                f.write("------------------------------------------------------\n\n")

# Example usage
if __name__ == "__main__":
    # Grab news from RBC
    rbc_grabber = RBCNewsGrabber("http://static.feed.rbc.ru/rbc/logical/footer/news.rss")
    news_list = rbc_grabber.fetch_news()

    # Grab jokes
    jokes_grabber = JokesGrabber("jokes_cache.json")
    jokes_list = jokes_grabber.fetch_jokes("https://www.anekdot.ru/random/anekdot")

    # Generate troll news
    troll_factory = TrollFactory(jokes_list)
    troll_news = troll_factory.generate_troll_news(news_list)

    # Save to file
    NewsSaver.save_to_file(troll_news, "troll_news.txt")

    print("Troll news has been generated and saved to troll_news.txt.")
