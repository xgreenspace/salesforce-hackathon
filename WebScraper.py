import os
import sys

import requests
from bs4 import BeautifulSoup


class TalentSearch():
    def __init__(self, job=-1):

        # Gets web content from a linkedIn List pretaining to a specific job search.
        jobs = {0:'Computer Software', 1:'Internet', 2:'Oil & Energy', 3:'Information Technology & Services', \
            4:'Electrical & Electronic Manufacturing'}

        if jobs[job] == 'Computer Software':
            result = requests.get('https://www.linkedin.com/search/results/people/?facetIndustry=%5B%224%22%5D&origin=FACETED_SEARCH')
        elif jobs[job] == 'Internet':
            result = requests.get('https://www.linkedin.com/search/results/people/?facetIndustry=%5B%226%22%5D&origin=FACETED_SEARCH')
        elif jobs[job] == 'Oil & Energy':
            result = requests.get('https://www.linkedin.com/search/results/people/?facetIndustry=%5B%2257%22%5D&origin=FACETED_SEARCH')
        elif jobs[job] == 'Information Technology & Services':
            result = requests.get('https://www.linkedin.com/search/results/people/?facetIndustry=%5B%2296%22%5D&origin=FACETED_SEARCH')
        elif jobs[job] == 'Electrical & Electronic Manufacturing':
            result = requests.get('https://www.linkedin.com/search/results/people/?facetIndustry=%5B%22112%22%5D&origin=FACETED_SEARCH')
        else: 
            result = ''

        # Accesses the website and assigns the data to a variable
        src = result.content
        soup = BeautifulSoup(src, 'html5lib')

        canidates_names = soup.find_all('span', attrs={'class':'name actor-name'})

        pretty = soup.prettify()

        print(type(pretty))

        with open('page.html', 'w', encoding='utf-8') as f:
            f.write(pretty)




app1 = TalentSearch(2)
