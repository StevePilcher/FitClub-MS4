from django.http import HttpResponse


class StripeWH_Handler:
    """ Handle Stipe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle unexpected Webhook responses """
        return HttpResponse(
            content=f'Unhandled Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle payment_intent.succeeded webhook from Stripe"""
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """ Handle payment_intent.payment_failed webhook from Stripe """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
