from django.contrib.auth import get_user_model

User = get_user_model()
random = User.objects.last()

random_profile.followers.all()
random_.is_following.all()