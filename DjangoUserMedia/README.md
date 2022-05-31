# Django User Media
You have simple Django project with one application `users`.

In this application you have one Django model `Profile` with relation 1-1 to Django User model.

So, the task is to add 2 fields to `Profile` model: 
1) `avatar` - image field that should be available for everyone to see.
2) `eye_key` - image field that should be available only for current user to see.