from django.db import models


class Organization(models.Model):
    """
    An entity that owns a couple of bank accounts.  For instance, a household.
    """

    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Account(models.Model):
    """
    A bank account.  The account has an account name and an account number.
    """

    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100, unique=True)

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number}"


class Transfer(models.Model):
    """
    A bank transfer.  The transfer is done from a bank account to a specific recipient.
    The recipient may or may not be an account numer, a name, or anything else.
    """

    reference = models.CharField(max_length=100)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    recipient = models.CharField(max_length=100)

    amount = models.IntegerField(help_text='in cents',)
    date = models.DateField()
    comment = models.TextField()

    CATEGORY_CHOICES = (
        ('food', 'Food'),
        ('house', 'House'),
        ('hobbies', 'Hobbies'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"({self.reference}, {self.account}, {self.recipient}, {self.amount / 100:.2f}Eur, {self.date}, {self.comment}"
