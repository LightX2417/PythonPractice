from django import forms
from .models import Book, Author, Publisher, BookPublisher


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "publication_date", "author", "publishers"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customizing the form fields if necessary
        self.fields["publishers"].queryset = Publisher.objects.all()

    def save(self, commit=True):
        book = super().save(commit=False)
        if commit:
            book.save()
        # Handle the many-to-many relationship
        publishers = self.cleaned_data["publishers"]
        for publisher in publishers:
            BookPublisher.objects.create(
                book=book, publisher=publisher, published_date=book.publication_date
            )
        return book


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ["name", "address"]


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "birthdate"]
