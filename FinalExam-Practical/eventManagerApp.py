from event import Events


def run():
    global event
    event = Events.loadDataFromFile
 
    while True:
        menu = print('1.Add regular Event \n2.Add Special Event \n3.Calculate All Event Fees 4.Exit')
        choice = int(input('What would you like to do(1-4)?: '))

        if choice == 1:
            category = 'Regular Event'

        if choice == 2:
            pass
        
        if choice == 3:
            pass

        if choice ==4:
            print('Thank you!')
            exit()




