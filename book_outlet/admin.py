from django import forms
from django.contrib import admin
from .models import Book, Author, Address, Publication

# Register your models here.


class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            "published_from": forms.CheckboxSelectMultiple()  # Ensures no auto-selection
        }


class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author",)


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Publication)
