from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

# pip install misaka
import misaka

from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()

#------------------------------------------------------------------------------------------
#                               ** Post Model **
# This model stores all the information for a post including the user, when it was created,
# the message of the post, the group the post belongs to, and the number of likes it has
#------------------------------------------------------------------------------------------
class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts",null=True, blank=True,on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="group_post")

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user", "message"]


