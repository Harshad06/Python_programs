"""
Description
Environment Specifications & Instructions
Allowed Languages
Python3
Build Expectation

Problem Description

Write a script that scrapes the first five movie names from a web page, given by the variable url. 
Please use the variable name url to use the URL for scraping.

NOTE: To know the HTML file structure on the given website, please:

use browser-integrated Developer Tools, OR
use Inspect to view the source HTML.
TASK:

You have to implement imdb(url) function given in the code editor. Return a list of first five movies.
Sample URL: https://www.imdb.com/search/title/?year=2011&title_type=feature&

Sample Test Cases
Sample Input

url = "https://www.imdb.com/search/title/?year=2011&title_type=feature&"
Sample Output
------------------------
Crazy, Stupid, Love.
Harry Potter and the Deathly Hallows: Part 2
The Lincoln Lawyer
War Horse
The Cabin in the Wood
Note: Sample output may not match the actual website Output. The sample output is just for reference purposes.
"""

from bs4 import BeautifulSoup as bs
import requests

def imdb(url):
    pass