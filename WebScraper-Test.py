import requests
from bs4 import BeautifulSoup

def google():
    result = requests.get('https://www.google.com/')

    # Print if it's accessable
    print(result.status_code)

    # Print header
    print(result.headers)

    # Grap source of the page
    src = result.content

    # Pass source variable into BueatifulSoup
    soup = BeautifulSoup(src, 'html5lib')

    # Finds all the hyperlinks in a page
    links = soup.find_all('a')
    print(links)

    # Finds all hyperlinks with the word 'About'
    for link in links:
        if "About" in link.text:
            print(link)
            print(link.attrs['href'])


def white_house():
    result = requests.get('https://www.whitehouse.gov/briefings-statements/')
    src = result.content
    soup = BeautifulSoup(src, 'html5lib')

    urls = []
    for h2_tag in soup.find_all('h2'):
        a_tag = h2_tag.find('a')
        urls.append(a_tag.attrs['href'])

    print(urls)


def objects():
    