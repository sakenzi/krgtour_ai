from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Route
from django.shortcuts import render


def home(request):
    routes = [
        {"title": "Каркаралинские горы", "duration": "1 день", "difficulty": "Средний", "price": "Бесплатно",
         "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=60"},
        {"title": "Озеро Балхаш", "duration": "2 дня", "difficulty": "Лёгкий", "price": "15 000 ₸",
         "image": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=60"},
        {"title": "Бектау-Ата", "duration": "1 день", "difficulty": "Сложный", "price": "10 000 ₸",
         "image": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=1200&q=60"},
    ]
    return render(request, "routes/home.html", {"routes": routes})