import requests
from bs4 import BeautifulSoup

def get_word_meaning(word):
    url = 'https://www.dictionary.com/browse/{}'.format(word)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    meanings = soup.find_all('span', attrs={'class': 'one-click-content'})
    if meanings:
        return meanings[0].text.strip()
    return None

word = input('Enter a word: ')
meaning = get_word_meaning(word)
if meaning:
    print('The meaning of {} is: {}'.format(word, meaning))
else:
    print('Sorry, the meaning of {} could not be found.'.format(word))