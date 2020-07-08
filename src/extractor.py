from bs4 import BeautifulSoup
import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import re

#To create a valid unit test in code that uses random
# the same seed must be used every time
RAMDOM_SEED = 2020


#based on https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python
def text_from_html(html_text):
    html_text = html_text.decode("utf-8").encode("ascii","ignore")
    soup = BeautifulSoup(html_text)
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    # get text
    extracted_text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in extracted_text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    final_text = '\n'.join(chunk for chunk in chunks if chunk)
    return final_text

def count_devops(text):
    all_devops = re.findall("(?i)(devops)", text)
    return len(all_devops)

def create_word_cloud(text):
    cloud = WordCloud(background_color = "white", max_words = 200, stopwords = set(STOPWORDS), random_state = RAMDOM_SEED)
    cloud.generate(text)
    ##cloud.to_file("wordCloud.png")
    return cloud

def create_word_cloud_image(text, name):
    cloud = create_word_cloud(text)
    cloud.to_file(str(name)+".png")

def create_word_cloud_npArray(text):
    cloud = create_word_cloud(text)
    image_array = cloud.to_array()
    return image_array