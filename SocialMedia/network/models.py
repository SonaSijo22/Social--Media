from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save

# Create your models here.

class Profile(models.Model):

    name=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")

    profile_image=models.ImageField(upload_to="profile_images",default='blank-profile-picture.png',blank=True)

    bio=models.CharField(max_length=200)

    dob=models.DateField(null=True,blank=True)

    email=models.CharField(max_length=200,blank=True)

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    def _str_(self):
        return self.name.username
    
class Post(models.Model):

    user_object=models.ForeignKey(User,on_delete=models.CASCADE,related_name="post")

    caption=models.CharField(max_length=200)

    post_image=models.ImageField(upload_to="post_images",default="post_images/default.jpg",blank=True)

    like= models.ManyToManyField(User,related_name='postlikes',null=True)

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    def _str_(self):
        return self.user_object.username


    # @property
    # def like_count(self):
    #     likes_count=0
    #     for i in self.like.all():
    #         likes_count+=1
    #     return likes_count


class Like(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="likes")

    created_date=models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.user_object.username
    

    # @property
    # def like_count(self):
    #     li=self.objects.all()
    #     likes_count=0
    #     for i in li:
    #         likes_count+=1
    #     return likes_count

class Comment(models.Model):

    user_object=models.ForeignKey(User,on_delete=models.CASCADE)

    post_object=models.ForeignKey(Post,on_delete=models.CASCADE)

    comment=models.CharField(max_length=300)

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

    def _str_(self):
        return self.user_object.username

class Follower(models.Model):

  user=models.OneToOneField(User, on_delete=models.CASCADE)

  followers=models.ManyToManyField(User, related_name='following')

  created_date=models.DateTimeField(auto_now_add=True)

  def __str__(self):
      return self.user.username
  

def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(name=instance)
post_save.connect(sender=User,receiver=create_profile)