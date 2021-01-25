from django.db import models

# Create your models here.


class Vendor(models.Model):
    FAMILY = 'Family'
    BLANK = 'Not Applicable'
    YES = 'Yes'
    NO = 'No'
    BOOLEAN_CHOICES = [(BLANK, 'Not Applicable'), (YES, 'Yes'),
                       (NO, 'No'), (FAMILY, 'Family')]
    name = models.CharField(max_length=100, default='Type here')
    url = models.CharField(max_length=2048, default='Type here')
    area = models.CharField(max_length=100, default='Type here')
    notes = models.TextField()
    aesthetic = models.CharField(max_length=100, default=' ')
    country = models.CharField(max_length=15, default='N/A')
    state = models.CharField(max_length=15, default='N/A')
    wholesale = models.CharField(
        max_length=100, choices=BOOLEAN_CHOICES, default=BLANK)
    black_owned = models.CharField(max_length=100,
                                   choices=BOOLEAN_CHOICES, default=BLANK)
    minority_owned = models.CharField(max_length=100,
                                      choices=BOOLEAN_CHOICES, default=BLANK)
    woman_owned = models.CharField(max_length=100,
                                   choices=BOOLEAN_CHOICES, default=BLANK)
    small_business = models.CharField(max_length=100,
                                      choices=BOOLEAN_CHOICES, default=BLANK)
    sustainable = models.CharField(max_length=100,
                                   choices=BOOLEAN_CHOICES, default=BLANK)
    vegan = models.CharField(
        max_length=100, choices=BOOLEAN_CHOICES, default=BLANK)
    quarter_used = models.CharField(
        max_length=10, default='Enter Here')
    box_used = models.CharField(max_length=50, default='N/A')

    def __str__(self):
        return self.name


# class Info(models.Model):
#     vendor = models.ForeignKey(
#         Vendor, on_delete=models.CASCADE, related_name='info')
