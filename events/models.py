from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='')
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)

    def create_event(self):
        return {
            'summary': self.title,
            'location': self.location,
            'description': self.description,
            'start': {
                'dateTime': str(self.start_time),
                'timeZone': 'Asia/Shanghai',
            },
            'end': {
                'dateTime': str(self.end_time),
                'timeZone': 'Asia/Shanghai',
            },
            'reminders': {
                'useDefault': True,
            },
        }
