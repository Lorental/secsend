from django.db import models

# Create your models here.


class BaseModel(models.Model):
    create_date = models.DateTimeField('Added', auto_now_add=True)

    class Meta:
        abstract = True


class Message(BaseModel):
    identificator = models.TextField('Identificator', null=False, blank=False)
    message = models.TextField(null=True, blank=False)
    source_ip = models.TextField('Source IP',
                                 null=False,
                                 blank=False,
                                 default='Unknown')

    def __str__(self) -> str:
        return self.identificator


class Log(BaseModel):
    text = models.TextField('Log', null=False, blank=False)

    def __str__(self) -> str:
        return self.text
