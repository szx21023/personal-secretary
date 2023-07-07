from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .models import Event
from .utils import generate_calendar_credential

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def list_all(request):
    creds = generate_calendar_credential()
    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)

    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def create_event(request):
    if request.method != 'POST':
        return HttpResponse("Method not allow")

    creds = generate_calendar_credential()
    service = build('calendar', 'v3', credentials=creds)

    attr = request.POST.dict()

    event = Event(**attr)
    event.save()
    event = service.events().insert(calendarId='primary', body=event.create_event()).execute()

    print('Event created: %s' % event.get('htmlLink'))
    return HttpResponse("Successful created")

