from urllib.parse import quote_plus

from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render


def login(request):
    target_url = '/admin/login/'
    if next := request.GET.get("next"):
        target_url += f"?next={quote_plus(next)}"
    return redirect(target_url)


def logout(request):
    if request.method != "POST":
        return render(request, "patterns/auth/logout.html")
    auth_logout(request)
    return redirect("/")
