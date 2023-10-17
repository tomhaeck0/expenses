import csv
from datetime import datetime

from django.db import models


# Create your models here.
class Organization(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Account(models.Model):

    number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.number}"


class Transfer(models.Model):

    currency_choices = (("eur", "Eur"),)

    reference = models.CharField(max_length=100)

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    recipient = models.CharField(max_length=100)

    amount = models.IntegerField(help_text='in cents',)
    currency = models.CharField(max_length=20, choices=currency_choices)
    date = models.DateField()

    comment = models.TextField()

    def __str__(self):
        return f"({self.reference}, {self.account}, {self.recipient}, {self.amount}{self.currency}, {self.date}, {self.comment}"

    @classmethod
    def transfers_from_csv(cls, text_stream):

        csv_reader = csv.DictReader(text_stream)

        column_data_types = {
            'Referentie': str,
            'Rekening': str,
            'Naam tegenpartij': str,
            'Bedrag': float,
            'Munt': str,
            'Verrichtingsdatum': str,
            'Mededeling': str
        }

        column_names = {
            'Referentie': 'reference',
            'Rekening': 'account',
            'Naam tegenpartij': 'recipient',
            'Bedrag': 'amount',
            'Munt': 'currency',
            'Verrichtingsdatum': 'date',
            'Mededeling': 'comment'
        }

        transfers = []
        for transfer in csv_reader:

            transfer_normalized = {column_names[key]: column_data_types[key](value)
                                   for key, value in transfer.items() if key in column_data_types}

            transfer_normalized['amount'] = int(transfer_normalized['amount'] * 100)
            transfer_normalized['date'] = datetime.strptime(transfer_normalized['date'], "%d-%m-%Y").date()
            transfer_normalized['account'] = Account.objects.get(number=transfer_normalized['account'])

            transfers.append(Transfer(**transfer_normalized))

        return transfers


def main():
    file_path = '/home/tom/Workspace/Projects-2/expenses/python/src/expense_tracker/fixtures/example_data.csv'
    [transfer.save() for transfer in Transfer.transfers_from_csv(file_path)]


if __name__ == "__main__":
    main()

