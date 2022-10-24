from django.forms import ModelForm
from .models import AddAccomodation, Comment


class AddAccomodationForm(ModelForm):

    class Meta:
        model = AddAccomodation
        fields = [
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
                'addAccomodation_description',
                'addAccomodation_image',
                ]


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = [
                'text',
                ]
