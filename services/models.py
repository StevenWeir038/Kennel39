from django.db import models


class Service(models.Model):
    """
    Service model
    """
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=20, null=False, blank=False)
    service_desc = models.TextField(max_length=255, null=False, blank=False)

    def __str__(self):
        return str(self.service_name)
