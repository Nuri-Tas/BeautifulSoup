# ***BeautifulSoup***

from bs4 import BeautifulSoup  
import lxml
import requests

with open("/content/website.html") as file:
  content = file.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.prettify())

anchor_tag = soup.find_all("a")
for element in anchor_tag:
  print(element.get_text())

soup.find(id="name")

# extract all the links 

for link in soup.find_all("a"):
  print(link.get("href"))

# extract all the text in the page

print(soup.get_text())

soup.find_all(name="h1", id="name")
soup.find(name="h3").get("class")

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector=" #name")
print(name)

soup.select(selector=".heading")

# get all the anchor tags inside class_ 'simple'

select =soup.find_all("a")
print(select)

# extract only the anchor tags inside the unordered list in hall of fame

print(soup.select("li a"))


# ycombinator news 

response = requests.get(url="https://news.ycombinator.com/").text
print(response)
soup = BeautifulSoup(response, "html.parser")

links = soup.select(selector=".titlelink")
all_links = []
for link in links:
  all_links.append(link.get("href"))
all_links  

links_title = soup.select(selector=".titlelink")
titles = []
print(links_title)
for links in links_title:
  title = links.get_text()
  titles.append(title)

score_tag = soup.select(".score")
print(score_tag)

scores = []
score_id = {element.get("id"):  float(element.get_text().split(" ")[0])  for element in soup.select(".score")}
for id in score_id:
  scores.append(score_id[id])

max_index = scores.index(max(scores))
print(scores[max_index])
print(titles[17])
print(all_links[17])

for element in soup.select(".score"):
  print(element.get("id"))

# 100 Movies

response_movies = requests.get("https://www.empireonline.com/movies/features/best-movies-2/").text
print(response_movies)

soup = BeautifulSoup(response_movies, "html.parser")
print(soup)

all_films =soup.find_all(name="h3", class_="title")
print(all_films)

all_movies = soup.select(selector="p a")


film_tags = soup.find_all("a", target="_self", rel="noopener noreferrer")
print(film_tags)
films_and_reviews = [element.get_text()  for element in film_tags]

print(films_and_reviews)
splits = []
for element in films_and_reviews:
  split = element.split()
  splits.append(split)
print(splits)

films = []
for element in splits:
  print(element[0])
  if element[0] == "Read" and element[1] == "Empire's" and element[2] == "review":
    name = ""
    for character in element[4:]:
      print(character)
      name += f" {character}"
      print(name)
    films.append(name)
print(films)

films = films[::-1]
with open("films.txt", "w") as file:
  for movie in films:
    file.write(f"{movie}\n")
