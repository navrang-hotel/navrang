##
 # base/forms.py:
 #
 # St: 2018-03-16 Fri 09:35 PM
 # Up: 2018-03-16 Fri 09:35 PM
 #
 # Author: SPS
 ##

from django import forms

class FoodSearchForm(forms.Form):
    """Class for food search form."""

    keyword = forms.CharField(label="Keyword", max_length=100)


