from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail

# use to determine when to cal function in decorator
from django.db.models.signals import post_delete, post_save

# decorator to listen for events
from django.dispatch import receiver

from .forms import FORMS_YOU_NEED
from .models import MODELS_YOU_NEED

# example
@receiver(post_save, sender=MODEL)
def FUNC_NAME(sender, instance, created, **kwargs):
    # instance is object of MODEL
    # created is boolean True if object got created, False if object got updated
    # LOGIC HERE!
