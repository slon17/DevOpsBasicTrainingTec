import pytest
import os
from src.extractor import text_from_html
from src.extractor import count_devops


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

def test_devops_count():
	assert count_devops(text) == 147

