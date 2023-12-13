from event import Events

class SpecialEvents(Events, ):
    def add_event(eventType , eventID = str, eventLocation = str, category = str, fee = float, VIPFee = float):
        eventList = {'Event ID' : eventID, 'Event Location' : eventLocation, 'Category' : category, 'Fee' : fee, 'VIP Fee' : VIPFee}
        super().event[eventType].append(eventList)
        super(Events.saveDataToFile).saveDatatoFile()
        print(f'{eventType} has been added to {eventType}s!')


    def calculateEventFee():
        Fee = 0
        VIPFee = 0
        eventFee = float((super.fee + VIPFee)* 1.30)
        return eventFee
    

