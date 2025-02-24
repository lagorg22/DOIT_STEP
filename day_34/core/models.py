from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name
        

class Book(models.Model):
    title = models.CharField(max_length=50, null=False)
    page_count = models.PositiveIntegerField()
    publish_date = models.DateField()
    image = models.TextField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.title