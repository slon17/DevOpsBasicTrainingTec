import pytest
import os
from src.extractor import text_from_html
from src.extractor import create_word_cloud
from src.extractor import create_word_cloud_image
from src.extractor import create_word_cloud_npArray

#Load the html raw text ------------------------------------------------------------
script_dir = os.path.dirname(__file__)
relative_html_file_path = "Assets/DevOps-Wikipedia.html"
html_file_path = os.path.join(script_dir, relative_html_file_path)
f = open(html_file_path,"r")

html_text = f.read()
text = text_from_html(html_text)

#Start testing ----------------------------------------------------------------------
def test_text_loading():
	assert len(text) == 31086

def test_create_word_cloud():
	cloud = create_word_cloud(text)
	#print(str(type(cloud)))
	assert cloud is not None
	assert str(type(cloud)) == "<class 'wordcloud.wordcloud.WordCloud'>"

def test_array_word_cloud():
	np_image_array = create_word_cloud_npArray(text)
	assert (int(np_image_array.mean()) is not 219)
	assert (np_image_array.shape == (200,400,3))