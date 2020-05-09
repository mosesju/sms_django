from django.db import models

# Create your models here.
class Text(models.Model):
    # group = 
    text_body = models.CharField(max_length=160, null=True)
    name = models.CharField(max_length=160, null=True)
    # text_media should point to an S3 Bucket SET THIS UP WHEN THE TIME COMES
    text_media = models.CharField(max_length=200, null=True)
    send_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name