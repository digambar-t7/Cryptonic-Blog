from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    head1 = models.CharField(max_length=100)
    desc1 = models.CharField(max_length=5000)
    head2 = models.CharField(max_length=100)
    desc2 = models.CharField(max_length=5000)
    head3 = models.CharField(max_length=100)
    desc3 = models.CharField(max_length=5000)
    thumbnail = models.ImageField(upload_to='blog/images',default='')
    slug = models.CharField(max_length=100)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    # User generated fields
    # actual comment text
    comment = models.TextField()
    # user points to User obj from Model
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # post points to BlogPost obj from Model i.e. post = new BlogPost obj/instance
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    # parent itself is a BlogComment obj
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)

    # Automatically generated fields
    comment_id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username +' - '+self.comment