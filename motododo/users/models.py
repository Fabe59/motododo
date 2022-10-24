from django.db import models
from django.conf import settings
from accomodation.models import Accomodation


class Favorite(models.Model):

    accomodation_saved = models.ForeignKey(
                                        Accomodation,
                                        on_delete=models.CASCADE
                                        )
    user = models.ForeignKey(
                        settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE
                        )

    def __str__(self):
        return '{} - {}'.format(self.user, self.accomodation_saved)
