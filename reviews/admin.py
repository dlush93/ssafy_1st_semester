from django.contrib import admin
from .forms import ReviewForm
from .models import Review
# Register your models here.

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm