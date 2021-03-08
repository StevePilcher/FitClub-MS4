import json
import stripe
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from checkout.webhook_handler import StripeWH_Handler


@require_POST
@csrf_exempt
def my_webhook_view(request):
    """ Listen to webhooks from Stripe """
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(content=e, status=400)

    # Webhook Handler
    handler = StripeWH_Handler(request)

    # Connect Webhook events to relevant functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_failed,
    }

    # Get Webhook type from Stripe
    event_type = event['type']

    event_handler = event_map.get(event_type, handler.handle_event)

    # Call the event with this
    response = event_handler(event)
    return response
