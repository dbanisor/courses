from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")

yc_web_page = response.text.encode("utf-8")

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
# print(article_upvotes)

index_max_upvotes = article_upvotes.index(max(article_upvotes))
article_text_max_upvotes = article_texts[index_max_upvotes]
article_link_max_upvotes = article_links[index_max_upvotes]
print(index_max_upvotes)
print(article_text_max_upvotes)
print(article_link_max_upvotes)









# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)
#
# # for tag in all_anchor_tags:
# #     # print(tag.getText())
# #     print(tag.get("href"))
#
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.getText())
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(selector=".heading")
# print(headings)





















