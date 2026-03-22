from django.db import models


class Category(models.Model):
    CATEGORY_CHOICES = [
        ('coffee', 'Coffee'),
        ('noncoffee', 'Non-Coffee'),
        ('pastries', 'Pastries'),
        ('meals', 'Light Meals'),
    ]
    slug = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=True)
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    emoji = models.CharField(max_length=10, default='☕')
    image = models.ImageField(upload_to='menu/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} — ₱{self.price}'
