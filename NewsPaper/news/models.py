from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Author(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self, articles_rating, comments_by_author_rating, comments_to_author_rating):
        new_rating = articles_rating *3 + comments_by_author_rating + comments_to_author_rating
        self.rating = new_rating
        self.save()


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)


article = 'ART'
news = 'NWS'

POST_TYPES = [
    (article, 'статья'),
    (news, 'новость'),
]


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    type = models.CharField(max_length=3,
                            choices=POST_TYPES, )
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    header = models.TextField()
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return (self.text[:124]) + '...'



class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

