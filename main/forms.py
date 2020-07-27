from django import forms

from .models import Reviews


class ReviewForm(forms.ModelForm):
    """Leave a review"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")


# class RatingForm(forms.ModelForm):
#     """Add rating"""
#     star = forms.ModelChoiceField(
#         queryset=Rating.objects.all(), widget=forms.RadioSelect(), empty_label=None
#     )

#     class Meta:
#         model = Rating
#         fields = ("stars",)