import json 
from collections import defaultdict

class Events:

    events_file = 'events.json'

    event = defaultdict(list)

    def loadDataFromFile(events_file, event):
        try:
            with open(events_file, 'r') as file:
                return json.load(file)
            
        except FileNotFoundError:
            return defaultdict(list)


    def saveDataToFile(events_file, event):
        with open(events_file, 'w') as file:
            json.dump(event, file)

    def add_event(eventType , eventID = str, eventLocation = str, fee = float):
        eventList = {'Event ID' : eventID, 'Event Location' : eventLocation, 'Fee' : fee}
        super(Events.event).event[eventType].append(eventList)
        super(Events.saveDatatoFile).saveDatatoFile()
        print(f'{eventType} has been added to {eventType}s!')
        

    def calculateEventFee():
        Fee = 0
        eventFee = float(super.fee * 1.13)
        return eventFee
    
    def listEvents(events_file, event):
        items = event[super().eventType]
        if not items:
            print(f'{super().EventType} not found')
        else:
            for i, item in enumerate(items, start=1):
                print(f'{super().EventType} {i}: {item}')




