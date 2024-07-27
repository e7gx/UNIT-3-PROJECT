# Notifications/views.py

from django.http import HttpResponse
from Notifications.utils import send_alerts

def send_alerts_view(request):
    send_alerts()
    return HttpResponse('Alerts sent successfully')
