# newser
#
# PROGRAM MANIFEST
#
# Newser is an information feed. It automates the collection
# and display of information from a preset range(sources).
#
# It is produced with much assistance and some interference by chat-gpt.
#   
#
#
# 0.1.1 COMPLETE
#
# fetch news headlines and display in CLI [x]
#
# open articles in browser [x]
#
# print articles in CLI [x]
#
# 0.1.2 WORKING
#
# preset sources : hacker news [ ] r/news [ ] /news/ [ ] al jazeera [x]
#
# manual source input [ ]
# 
# 
# 
#
# custom date ranger [ ]
# 
# improve text-wrapping (adaptive hyphenation  [ ]
# 
#
#
#

version = '0.1.1'
init = True
from bs4 import BeautifulSoup
import requests, webbrowser, time


def fetch():
    url=("https://www.aljazeera.com")
    response = requests.get(url)
    if response.status_code != 200:
        print('Failed to retrieve {}'.format(url))

        return []

    soup = BeautifulSoup(response.content, "html.parser")
    headlines = []

    for article in soup.find_all("h3"):

        title = article.get_text(strip=True)
        parent_link = article.find_parent("a")
        if parent_link and "href" in parent_link.attrs:
            link = parent_link["href"]
            full_link = '{}{}'.format(url, link) if link.startswith('/') else link
            headlines.append((title, full_link))

    return headlines



def display_headlines(headlines):
    for idx, (title, link) in enumerate(headlines):
        print('{}. {}'.format(idx + 1, title))

    print("\nSelect an article number to read,or (q)uit.")

def main():
    headlines = fetch()
    print('\n')
    time.sleep(0.035)
    print('\n')
    time.sleep(0.035)
    print('\n')
    time.sleep(0.035)
    print('\n')
    time.sleep(0.035)
    print('\n')
    print('Welcome to Newser, version {}'.format(version))
    time.sleep(1.5)
    print('\n')


    

    if not headlines:
        return

    while True:
        display_headlines(headlines)

        choice = input("Enter article number or (q)uit.")
        if choice.lower() == 'q':
            time.sleep(0.5)
            print('Goodbye!')
            break

        try:
            choice = int(choice) - 1
            if choice < 0 or choice >= len(headlines):
                print('Invalid selection.')
                continue


            title, link = headlines[choice]
            action = input('\nSelected: {}\nOptions: \n1. Print in CLI\n2. Open in browser\n..')
            if action == '1':
                print_article_content(link)

            elif action == '2':
                webbrowser.open(link)
            else:
                print('Invalid input. Returning to headline selection.')

        except ValueError:
            print('Please enter a valid number.')


            

def print_article_content(url):
    response = requests.get(url)
    if response.status_code != 200:
        print('Article retrieval failed.')
        return


    soup = BeautifulSoup(response.content, "html.parser")


    paragraphs = soup.find_all("p")
    content = '\n'.join(p.get_text(strip=True) for p in paragraphs)

    print('\n--- Article Start ---\n')
    print(content[:50000])
    print('\n--- Article End ---\n')



if __name__ == "__main__":
    main()
                         
                  

