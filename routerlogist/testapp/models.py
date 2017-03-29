from django.db import models


class Mac(models.Model):
    address = models.CharField(max_length=17)
    log_date = models.DateTimeField('origin date')

    def __str__(self):
    	return self.address

