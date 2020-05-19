import requests
import json
from bs4 import BeautifulSoup

base_url = 'https://www.riddles.com/brain-teasers'
num_pages = 27

# JSON data to dump
data = {}
data['riddles'] = []

for i in range(1, num_pages + 1):
    query='?page=' + str(i)
    URL = base_url + query
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    # get global field pertaining to each question
    results = soup.find_all(itemtype='https://schema.org/Question')

    for res in results:
        # html class fields related to the riddle and its solution
        question_parser = res.find('blockquote', 
                class_='orange_dk_blockquote hidden-print')
        solution_parser = res.find('blockquote', class_='dark_purple_blockquote')
    
        question = question_parser.get_text()
        solution = solution_parser.get_text()
        
        # add data to JSON
        data['riddles'].append({
            'question': question,
            'solution': solution
            })

with open('riddles.json', 'w') as outfile:
    json.dump(data, outfile)
