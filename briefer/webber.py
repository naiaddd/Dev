# webber program manifest ---
#
# webber is a simple script which fetches a selection of websites for the user.
#
# 0.1.1 : fetch selected websites [x] add selected website [x]
#
# 0.1.2 : menu [x] quit button [x]
#
# 0.1.3 : clear presets [ ]
#
#
#

import webbrowser, requests, time

version = '0.1.2'



presets = ['https://en.wikiversity.org/wiki/Wikiversity:Featured', 'https://www.reddit.com']



def fetch():
    urls = presets
    for url in presets:
        webbrowser.open(url)
        

def add_preset():
    global presets 
    add = input('Enter URL to add: ')
    presets.append(add)


def main():
    init = True
    if init:
        print(f'Welcome to Webber, version {version}.')
    init = False
    
    while True:
        print(f'Current presets are {presets}')
        print('1. Open Presets')
        print('2. Add Preset')
        print('3. Clear presets')
        print('4. Exit program')
        reply = input('..')
        if reply == '1':
            fetch()
        elif reply == '2':
            add_preset()
        elif reply == '3':
            #presets = ['x']
            print('Functionality in progress...')
            time.sleep(1)
            print('Edit program file directly to delete presets.\n')
            time.sleep(1.5)
            pass
        elif reply == '4':
            print('Goodbye!')
            break
    




if __name__ == '__main__':
    main() 

'''
presets housing

https://en.wikiversity.org/wiki/Wikiversity:Featured

'''
