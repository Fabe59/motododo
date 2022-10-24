from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.name


class Parking(models.Model):
    parking = models.CharField(max_length=200, default=None)

    def __str__(self):
        return self.parking


class AddAccomodation(models.Model):
    addAccomodation_statut_list = (
        ("Non_lu", "Non lu"),
        ("Archive", "Archivé"),
    )

    addAccomodation_auto_increment_id = models.AutoField(primary_key=True)
    addAccomodation_name = models.CharField("Nom", max_length=128)
    addAccomodation_category = models.ForeignKey(
                                        Category,
                                        verbose_name=(
                                            "Categorie d'hébergement"
                                            ),
                                        on_delete=models.CASCADE
                                        )
    addAccomodation_number = models.PositiveSmallIntegerField(
                                        "Numéro",
                                        null=True,
                                        blank=True
                                        )
    addAccomodation_road = models.CharField("Adresse", max_length=250)
    addAccomodation_zipcode = models.PositiveIntegerField("Code Postal")
    addAccomodation_city = models.CharField("Ville", max_length=50)
    addAccomodation_phone = models.CharField("Téléphone", max_length=10)
    addAccomodation_email = models.EmailField("Email")
    addAccomodation_url = models.URLField("URL", null=True, blank=True)
    addAccomodation_parking = models.ForeignKey(
                                        Parking,
                                        verbose_name=('Type de Parking'),
                                        on_delete=models.CASCADE
                                        )
    addAccomodation_image = models.ImageField(
                                    "Image",
                                    null=True,
                                    blank=True,
                                    upload_to="accomodation/",
                                    default="default_accomodation_image.jpg"
                                    )
    addAccomodation_description = models.CharField(
                                            'Description',
                                            max_length=250
                                            )
    addAccomodation_statut = models.CharField(
                                        "Statut de la demande",
                                        choices=addAccomodation_statut_list,
                                        max_length=16,
                                        default="Non_lu"
                                        )

    def __str__(self):
        return '{}'.format(self.addAccomodation_name)


class Accomodation(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    road = models.CharField(max_length=250)
    zipcode = models.PositiveIntegerField()
    city = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    url = models.CharField(max_length=250, null=True, blank=True)
    park = models.ForeignKey(Parking, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=250)
    lat = models.DecimalField(
                    max_digits=11,
                    decimal_places=6,
                    null=True,
                    blank=True
                    )
    lon = models.DecimalField(
        max_digits=11,
        decimal_places=6,
        null=True,
        blank=True
        )
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def save(self, *args, **kwargs):
        self.city = self.city.title()
        return super(Accomodation, self).save(*args, **kwargs)

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse(
                "accomodation:details",
                kwargs={"id": self.auto_increment_id}
                )

    def __str__(self):
        return '{}, {} {}, {}, {} - {}, {}'.format(
                                                self.name,
                                                self.number,
                                                self.road,
                                                self.zipcode,
                                                self.city,
                                                self.lat,
                                                self.lon
                                                )


class Comment(models.Model):
    accomodation = models.ForeignKey(Accomodation, on_delete=models.CASCADE)
    user = models.ForeignKey(
                    settings.AUTH_USER_MODEL,
                    on_delete=models.CASCADE
                    )
    text = models.TextField(
                    "Commentaire",
                    max_length=200
                    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - {} : {}'.format(
                                self.user,
                                self.accomodation.name,
                                self.text
                                )
