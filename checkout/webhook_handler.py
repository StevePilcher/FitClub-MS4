from django.http import HttpResponse


class stripeWH_Handler:
    """ Handle Stipe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle unexpected Webhook responses """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
