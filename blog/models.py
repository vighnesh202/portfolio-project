from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __self__(self):
        return self.title
    
    def pub_date_modified(self):
        return self.pub_date.strftime('%b %e %Y')