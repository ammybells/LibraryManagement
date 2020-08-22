from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookList(models.Model):
    book_name = models.CharField(max_length = 50)
    book_description = models.TextField()
    book_image = models.ImageField(upload_to = 'pics', default = 'img.jpg', blank = True, null = True)
    borrowed_by = models.ForeignKey(User, on_delete = models.CASCADE , null=True, blank =True)



    class Meta:
        verbose_name_plural = 'BookList'


    def __str__(self):
        return self.book_name