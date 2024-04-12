# Create "static" folder in root directory with "js", "css" etc folders.

# settings.py

STATIC_URL = "static/"

# create

STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = [BASE_DIR / "static"]


# usage

{% load static %} # top

<link rel="stylesheet" href="{% static 'css/main.css' %}"> # head
