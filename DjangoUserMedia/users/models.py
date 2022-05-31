from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

    # add avatar image and eye personal private image fields here

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
