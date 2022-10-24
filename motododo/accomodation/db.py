from accomodation.constants import CATEGORIES, PARKING
from accomodation.models import Category, Parking


class Database:

    def get_categories(self):
        """Add categories in database"""

        for cat in CATEGORIES:
            Category.objects.create(name=cat)

    def get_parking(self):
        """Add parking in database"""

        for park in PARKING:
            Parking.objects.create(parking=park)
