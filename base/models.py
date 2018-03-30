from django.db import models

# Create your models here.

# =============================
# Added by developer after this
# =============================

from datetime import datetime

# ====
# Menu
# ====

class MenuCategory(models.Model):
    """Class for menu_category model."""

    title = models.CharField(max_length=100)

    def __str__(self):
        """String representation of the model."""

        return self.title

class MenuItem(models.Model):
    """Class for menu_item model."""

    name = models.CharField(max_length=100)
    menu_category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField(max_length=500)

    def __str__(self):
        """String representation of the model."""

        return self.name

# ======
# Review
# ======

class Review(models.Model):
    """Class for review model."""

    reviewer_name = models.CharField(max_length=100)
    reviewer_email = models.EmailField(max_length=100)
    comment = models.TextField(max_length=500)
    star_rating = models.IntegerField()
    date_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        """String representation of the model."""

        return self.reviewer_name

# ===============
# Contact Message
# ===============

class ContactMessage(models.Model):
    """Class for contact message model."""

    sender_name = models.CharField(max_length=100)
    sender_email = models.EmailField(max_length=100)
    message = models.TextField(max_length=500)
    date_time = models.DateTimeField(default=datetime.now)

    STATUS = (
        ('N', 'News',),
        ('P', 'Progress',),
        ('R', 'Replied',),
    )

    status = models.CharField(max_length=1, choices=STATUS)

    def __str__(self):
        """String representation of the model."""

        return self.sender_name
