from abc import ABCMeta, abstractmethod


class Trip(metaclass=ABCMeta):
    @abstractmethod
    def setTransport(self):
        pass

    @abstractmethod
    def day(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def returnHome(self):
        pass

    def itinerary(self):
        self.setTransport()
        self.day()
        self.day2()
        self.day3()
        self.returnHome()


class VeniceTrip(Trip):
    def setTransport(self):
        print('Take a boat and find your way in the grant Canal.')

    def day(self):
        print('Visit St Mark`s Basilica in St Mark`s Square.')

    def day2(self):
        print('Appraciate Doge`s Palace.')

    def day3(self):
        print('Enjoy food near Rialto Bridge.')

    def returnHome(self):
        print('Get soveniers for friends and get back.')


class MaldivesTrip(Trip):
    def setTransport(self):
        print('On food, on any island, Wow!')

    def day(self):
        print('Enjoy the marine life of Banana Reef.')

    def day2(self):
        print('Go for the water sports and snorkelling.')

    def day3(self):
        print('Relax on the beach an enjoy the sun.')

    def returnHome(self):
        print('Don`t fell like leaving the beach.')


class TravelAgency:
    def arrange_trip(self):
        choice = input('What kind of place you`d like to go?historical or beach?')
        if choice == 'historical':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        if choice == 'beach':
            self.trip = MaldivesTrip()
            self.trip.itinerary()


TravelAgency().arrange_trip()
