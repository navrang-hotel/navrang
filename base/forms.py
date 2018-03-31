##
 # base/forms.py:
 #
 # St: 2018-03-16 Fri 09:35 PM
 # Up: 2018-03-16 Fri 09:35 PM
 #
 # Author: SPS
 ##

from django import forms

from .models import ContactMessage, Review

class FoodSearchForm(forms.Form):
    """Class for food search form."""

    keyword = forms.CharField(label="Keyword", max_length=100)

class ContactMessageForm(forms.ModelForm):
    """Class for contact message model form."""

    # Add class style, and html attributes to sender_name textinput widget
    sender_name = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'class':"form-control",
                'id':'sname',
                'name':'sname',
                'placeholder':'Name',
                'type': 'text',
            }
            # class="form-control" id="email" name="email" placeholder="Email" type="email"
        )
    )

    # Add class style, and html attributes to sender_email textinput widget
    sender_email = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'class':"form-control",
                'id':'email',
                'name':'email',
                'placeholder':'Email',
                'type': 'email',
            }
            # class="form-control" id="email" name="email" placeholder="Email" type="email"
        )
    )

    # Add class style, and html attributes to message textarea widget
    message = forms.CharField(
    # ^ ?But this is text field?
        widget=forms.Textarea(
            attrs = {
                'class':"form-control",
                'id':'comments',
                'name':'comments',
                'placeholder':'Comment',
                'rows':'5',
            }
        )
    )

    class Meta:
        model = ContactMessage
        fields = [
            'sender_name',
            'sender_email',
            'message',
        ]

class ReviewForm(forms.ModelForm):
    """Class for contact review form."""

    # reviewer_name = models.CharField(max_length=100)
    # reviewer_email = models.EmailField(max_length=100)
    # comment = models.TextField(max_length=500)
    # star_rating = models.IntegerField()
    # date_time = models.DateTimeField(default=datetime.now)

    # Add class style, and html attributes to reviewer_name textinput widget
    reviewer_name = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'class':"form-control",
                'id':'rname',
                'name':'rname',
                'placeholder':'Name',
                'type': 'text',
            }
            # class="form-control" id="email" name="email" placeholder="Email" type="email"
        )
    )

    # Add class style, and html attributes to reviewer_email textinput widget
    reviewer_email = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'class':"form-control",
                'id':'email',
                'name':'email',
                'placeholder':'Email',
                'type': 'email',
            }
            # class="form-control" id="email" name="email" placeholder="Email" type="email"
        )
    )

    # Add class style, and html attributes to message textarea widget
    comment = forms.CharField(
    # ^ ?But this is text field?
        widget=forms.Textarea(
            attrs = {
                'class':"form-control",
                'id':'comments',
                'name':'comments',
                'placeholder':'Comment',
                'rows':'5',
            }
        )
    )

    # Add class style, and html attributes to star rating number widget
    star_rating = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                'class':"form-control nb-tm-10px",
                'id':'srating',
                'name':'srating',
                'placeholder':'Stars',
                'type': 'number',
            }
        )
    )

    class Meta:
        model = Review
        fields = [
            'reviewer_name',
            'reviewer_email',
            'comment',
            'star_rating',
        ]

