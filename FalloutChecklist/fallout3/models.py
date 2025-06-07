from django.db import models


class Quest(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    available = models.TextField(blank=True, null=True)
    acquired = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    found = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    repeatable = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Bobblehead(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    acquired = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class SkillBook(models.Model):
    title = models.CharField(max_length=128)
    name = models.CharField(max_length=64)
    count_found = models.IntegerField(default=0)
    count_total = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}: {self.title}"


class RareItem(models.Model):
    title = models.CharField(max_length=128)
    note = models.CharField(max_length=255, blank=True)
    acquired = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.note}" if self.note else self.title


class AlienCaptiveLog(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=64)
    notes = models.TextField(blank=True)
    acquired = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class NukaColaQuantum(models.Model):
    title = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    count_found = models.IntegerField(default=0)
    count_total = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} - {self.location}"


class Clothing(models.Model):
    title = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    acquired = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.name}"


class Weapon(models.Model):
    title = models.CharField(max_length=64)
    name = models.CharField(max_length=128)
    acquired = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.name}"


class TeddyBear(models.Model):
    title = models.CharField(max_length=64)
    location = models.CharField(max_length=128)
    notes = models.TextField(blank=True)
    count_found = models.IntegerField(default=0)
    count_total = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.title} - {self.location}"
