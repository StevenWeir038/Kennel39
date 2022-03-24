from django.db import models


class Services(models.Model):
    """
    Services model
    """
    service_name = models.CharField(max_length=20, null=False, blank=False)
    service_desc = models.TextField(max_length=255, null=False, blank=False)

    def _str__(self):
        return self.service_name
