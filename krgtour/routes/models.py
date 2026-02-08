from django.db import models
from django.conf import settings



class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="places/", blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Route(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration_hours = models.DecimalField(max_digits=5, decimal_places=2, default=2)
    difficulty = models.CharField(
        max_length=20,
        choices=[("easy", "Easy"), ("medium", "Medium"), ("hard", "Hard")],
        default="easy",
    )
    places = models.ManyToManyField(Place, related_name="routes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user} → {self.route} ({self.rating})"