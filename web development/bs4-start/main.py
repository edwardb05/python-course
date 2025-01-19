from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title.name)

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id = "name")
print(heading.get_text())

url = soup.select_one(selector="p a")
print(url)