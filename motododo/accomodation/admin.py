from django.contrib import admin
from accomodation.models import Category,\
                                Parking,\
                                Accomodation,\
                                AddAccomodation,\
                                Comment

admin.site.register(Category)
admin.site.register(Parking)
admin.site.register(Accomodation)
admin.site.register(Comment)


class AddAccomodation_Admin(admin.ModelAdmin):
    list_display = (
        'addAccomodation_name',
        'addAccomodation_category',
        'addAccomodation_number',
        'addAccomodation_road',
        'addAccomodation_zipcode',
        'addAccomodation_city',
        'addAccomodation_phone',
        'addAccomodation_email',
        'addAccomodation_url',
        'addAccomodation_parking',
        'addAccomodation_statut',
    )

    list_filter = ('addAccomodation_statut',)


admin.site.register(AddAccomodation, AddAccomodation_Admin)
