from .models import Activity, Flight, Hotel, Ticket
from django_countries import countries


def getTicketsArray():
    tickets = []
    startTickets = Ticket.objects.all().values()[:3]
    activeTickets = []

    for ticket in startTickets:
        ticket["discounted"] = ticket["price"] - (
            ticket["discount"] * ticket["price"] / 100
        )
        activeTickets.append(ticket)

    allTickets = Ticket.objects.all().values()[3:]
    numTickets = []
    j = -1
    for i in range(len(allTickets)):
        if i % 3 == 0:
            j += 1
            tickets.append([])
            numTickets.append(j + 1)
        ticket = allTickets[i]
        ticket["discounted"] = ticket["price"] - (
            ticket["discount"] * ticket["price"] / 100
        )
        tickets[j].append(ticket)

    return activeTickets, numTickets, tickets


def getPackagesArray():
    myCountries = Ticket.objects.order_by("country").values("country").distinct()
    packages = []
    for country in myCountries:
        tickets = Ticket.objects.filter(country=country["country"])
        numPackages = len(tickets)
        picture = tickets[0].picture
        packages.append(
            {
                "country": dict(countries)[country["country"]],
                "picture": picture,
                "numPackages": numPackages,
            }
        )
    packages = sorted(packages, key=lambda k: k["numPackages"], reverse=True)
    return packages


def getFeaturedTrips():
    featuredTrips = Ticket.objects.filter(trending=True)
    activeTrip = featuredTrips[0]
    trips = featuredTrips[1:]
    numTrips = [i for i in range(1, len(trips) + 1)]
    return activeTrip, numTrips, trips


def getActivities():
    allActivities = Activity.objects.all()
    activeActivity = allActivities[0]
    activities = allActivities[1:]
    numActivities = [i for i in range(1, len(activities) + 1)]
    return activeActivity, numActivities, activities


def getHotels():
    allHotels = Hotel.objects.all()
    return allHotels


def getFlights():
    allFlights = Flight.objects.all()
    return allFlights