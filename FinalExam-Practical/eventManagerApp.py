from event import Events
from specialEvent import SpecialEvents


def run():
    global event
    event = Events.loadDataFromFile
 
    while True:
        menu = print('\n1.Add regular Event \n2.Add Special Event \n3.Calculate All Event Fees \n4.Show Event(s) \n5.Exit')
        choice = int(input('\nWhat would you like to do(1-5)?: '))

        if choice == 1:
                EventType = 'Regular Event'
                eventID = input('Enter event ID: ')
                eventLocation = input('Enter event location: ')
                fee = input('Enter Regular Event fee: ')
                Events.add_event(eventID, eventLocation, fee)

        elif choice == 2:
                EventType = 'Special Event'
                eventID = input('Enter event ID: ')
                eventLocation = input('Enter event location: ')
                category = input('Enter event category (Wedding/Birthday/etc): ')
                fee = input('Enter Special Event fee: ')
                VIPFee = input('Enter VIP Event Fees')
                SpecialEvents.add_event(eventID, eventLocation, category, fee, VIPFee)


        elif choice == 3:
            EventType = input('Please Enter Event Type(Regular Event/Special Event): ')

            while True:
                if EventType == 'Special Event':
                    SpecialEvents.calculateEventFee()
                    break
                elif EventType == 'Regular Event':
                    Events.calculateEventFee()
                    break
                else:
                    print('Please enter a valid selection.')
            

        elif choice == 4:
            while True:
                EventType = input('Enter event type (Regular Event/Special Event): ').lower()

                if EventType == 'Regular Event' or 'Special Event':
                    Events.loadDataFromFile(EventType)
                    break
                else:
                    print('Please enter a valid choice.')

        elif choice == 5:
            print('Thank you!')
            exit()

        else:
            print('Pleaase print a valid choice.')


run()



