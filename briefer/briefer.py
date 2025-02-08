## briefer


###### program manifest #######


# briefer is a productivity and information hub program.
# it serves as a meta-program which centralises and automates access
# to the functionality of other programs.



version = '0.0.1'

print(f'Welcome to Briefer, version {version}\n')


import webber, tasker, time, newser, weatherer



weatherer.presets()

def main():
    while True:
        print('What would you like to do?')
        print('1. Open Webber')
        print('2. Open Tasker')
        print('3. Open Logger')
        print('4. Open Newser')
        print('5. Open Weatherer')
        print('6. Briefing program')
        print('7. Exit Briefer')
        reply = input('..')
        if reply == '1':
            webber.main()
        elif reply =='2':
            tasker.main()
        elif reply == '3':
            print('Func in dev')
            pass
        elif reply == '4':
            newser.main()
            pass
        elif reply == '5':
            weatherer.main()
        elif reply == '7':
            print('exiting...')
            time.sleep(0.8)
            break
        else:
            print('Func in dev...\n')
            time.sleep(1)
            
            pass
            
        
        

    









if __name__ == '__main__':
    main()
