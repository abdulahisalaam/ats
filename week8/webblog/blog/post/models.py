from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User



class ActivePostManager(models.Manager):
    def get_queryset(self):
        return super(ActivePostManager, self).get_queryset().filter(is_hidden = True)


class InActivePostManager(models.Manager):
    def get_queryset(self):
        return super(InActivePostManager, self).get_queryset().filter(is_hidden = False)


class Tag(models.Model):
  name = models.CharField(max_length=40)

  def __str__(self):
      return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='usr')
    bio = models.TextField()
    avatar = models.ImageField(upload_to='media',default='default.jfif')

    def __str__ (self):
        return str(self.user)



class Post(models.Model):
    STATUS_CHOICES = (('published','Published'),('draft','Draft'))
    
    title = models.CharField(max_length=250)
    slug= models.SlugField(max_length=250, unique =True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_poster')
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to='post/media/', blank=True, null=True, default='default.jpg',help_text='upload image')
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')
    is_hidden = models.BooleanField(default= False) 
    
    objects = models.Manager()
    delete_objects = ActivePostManager()
    active_objects = InActivePostManager()

    class meta:
        ordering = ['-publish']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this Post."""
        return reverse('home')


class Comment(models.Model):
    
    body = models.TextField()
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')

    publish = models.DateTimeField(default=timezone.now)
    
    created = models.DateTimeField(auto_now_add = True)
    
    active = models.BooleanField(default=False)

    comments = models.ForeignKey('Comment',on_delete = models.CASCADE, related_name='postcomments')

    class meta:
        ordering = ('-publish')
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.post.title, self.user.username)