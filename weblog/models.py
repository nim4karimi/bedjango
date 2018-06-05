from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(allow_unicode=True,unique=True)
    pic = models.ImageField(upload_to='posts/')
    body = models.TextField()
    pub_date = models.DateField(auto_now=True)
    mod_date = models.DateField(auto_now_add=False)

    # __ Show in String __
    def __str__(self):
        return self.title

    # # __ Get Right Url ___
    # def get_absolute_url(self):
    #     return "/posts/%s/" % self.slug

