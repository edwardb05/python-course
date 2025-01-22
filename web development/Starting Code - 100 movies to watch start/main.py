import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
text = requests.get(URL).text

soup = BeautifulSoup(text, "html.parser")
movies = soup.find_all('h3', class_ = 'title')
movie_titles = [movie.getText() for movie in movies]

with open("100movies.txt", "w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")

