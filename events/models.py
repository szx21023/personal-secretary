from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)

    def create_event(self):
        return {
            'summary': self.title,
            'location': self.location,
            'description': self.description,
            'start': {
                'dateTime': self.start_time,
                'timeZone': 'Asia/Shanghai',
            },
            'end': {
                'dateTime': self.end_time,
                'timeZone': 'Asia/Shanghai',
            },
            'reminders': {
                'useDefault': True,
            },
        }
