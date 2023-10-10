from django.db import models


# Create your models here.
class Organization(models.Model):

    name = models.CharField(max_length=100)


class Account(models.Model):

    number = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)


class Transfer(models.Model):

    type_choices = (("sepa", "SEPA-domiciliëring"),)
    currency_choices = (("eur", "Eur"),)

    reference = models.CharField(max_length=100)

    account_from = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transfers_from")
    account_to = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transfers_to")

    amount = models.IntegerField(help_text='in cents',)
    currency = models.CharField(max_length=20, choices=currency_choices)
    date = models.DateField()
    description = models.CharField(max_length=100, choices=type_choices)

    comment = models.TextField()
