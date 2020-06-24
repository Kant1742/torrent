from django import forms

from .models import Reviews, Rating


class ReviewForm(forms.ModelForm):
    """Leave a review"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


# class RatingForm(forms.ModelForm):
#     """Add rating"""
#     star = forms.ModelChoiceField(
#         queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
#     )

#     class Meta:
#         model = Rating
#         fields = ("star",)