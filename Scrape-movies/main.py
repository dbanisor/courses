from bs4 import BeautifulSoup


WEB_FILE = "100_best_movies.html"


def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        print(f"You need to save the rendered HTML to {WEB_FILE}")
        exit()
    finally:
        with open(WEB_FILE, mode="r", encoding="iso-8859-1") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")


soup = read_web_file()

all_movies = soup.find_all(name="h3", class_="jsx-4245974604")

all_titles = [title.getText() for title in all_movies]
movies = all_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")