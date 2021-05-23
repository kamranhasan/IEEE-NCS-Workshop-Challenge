from .models import Ticket


def getTicketsArray():
    tickets = []
    activeTickets = Ticket.objects.all()[:3]
    allTickets = Ticket.objects.all()[3:]
    numTickets = []
    j = -1
    for i in range(len(allTickets)):
        if i % 3 == 0:
            j += 1
            tickets.append([])
            numTickets.append(j + 1)
        tickets[j].append(allTickets[i])
    return activeTickets, numTickets, tickets
