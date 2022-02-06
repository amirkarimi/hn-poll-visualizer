#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import termplotlib as tpl
import argparse

parser = argparse.ArgumentParser(description='Visualize HackerNews polls.')
parser.add_argument('url', metavar='URL', type=str, help='HackerNews URL')
args = parser.parse_args()
if not args.url.startswith('https://news.ycombinator.com/item'):
  print("Error: The URL doesn't seem to belong to HackerNews.")
  exit(1)

r = requests.get(args.url)
soup = BeautifulSoup(r.content, 'html.parser')

def process(soup):
  for row in soup.select('table table table > tr.athing'):
    value = row.find('font').text
    score = row.next_sibling.select_one('.score').text.strip(' points')
    yield (int(score), value)

list = sorted(process(soup), reverse=True)
if not list:
  print("Error: Couldn't parse the data. Are you sure it's a poll? Check the URL and try again.")
  exit(1)

data = [s for s, v in list]
label = [v for s, v in list]

fig = tpl.figure()
fig.barh(data, label, force_ascii=False)
fig.show()
