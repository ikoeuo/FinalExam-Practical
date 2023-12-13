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

    def add_event(eventType , eventID = str, eventLocation = str, category = str):
        eventList = {'Event ID' : eventID, 'Event Location' : eventLocation, 'Category' : category}
        super.event[eventType].append(eventList)
        super.saveDatatoFile()
        print(f'{eventType} has been added to Events!')
        

    def calculateEventFee():
        Fee = 0
        eventFee = Fee * 1.13
        return eventFee
    





