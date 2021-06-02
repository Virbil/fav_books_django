from django.db import models
from login_reg_app.models import User

class Book_Manager(models.Manager):
    def duplicate_check(self, post_data):
        errors = {}
        duplicate = Book.objects.filter(title=post_data['title'])
        
        if duplicate:
            errors['title'] = "This title is already entered"

        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
        # OTM - the user who uploaded a given book
    user_who_favorited = models.ManyToManyField(User, related_name="favorited_books")
        # MTM - a list of users who favorited a given book
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = Book_Manager()