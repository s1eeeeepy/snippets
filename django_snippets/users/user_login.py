# login view

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# name cannot be just "login", it will cause conflict with imported method
def user_login(reqest):
    # can;t reach page if user is logged in
    if request.user.is_authenticated:
        return redirect("URL_NAME")
    if request.method == "POST"
        # set vars from POST data
        username = request.POST["username"].lower()
        password = request.POST["password"]
        # check if user exists
        try:
            user = User.objects.get(username=username)
        except:
            # drop error
        # set auth data
        user = authenticate(request, username=username, password=password)
        # check if user and password matching
        if user is not None:
            login(request, user)
            return redirect("URL_NAME")
        else:
            # drop error
    return render(request, "HTML_PATH")
