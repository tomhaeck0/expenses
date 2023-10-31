import csv

from datetime import datetime
from dataclasses import dataclass

from expense_tracker.models import Account, Transfer


@dataclass(frozen=True)
class Argenta:

    csv_def = {
        'Referentie': (str, 'reference'),
        'Rekening': (str, 'account'),
        'Naam tegenpartij': (str, 'recipient'),
        'Bedrag': (float, 'amount'),
        'Verrichtingsdatum': (str, 'date'),
        'Mededeling': (str, 'comment'),
    }


def transfers_from_csv(cls, text_stream, bank=Argenta):

    csv_reader = csv.DictReader(text_stream)

    transfers = []
    for csv_transfer in csv_reader:

        transfer = {bank.csv_def[key][1]: bank.csv_def[key][0](value)
                    for key, value in csv_transfer.items() if key in bank.csv_def}

        # a couple of additional modifications
        transfer['amount'] = int(transfer['amount'] * 100)
        transfer['date'] = datetime.strptime(transfer['date'], "%d-%m-%Y").date()
        try:
            transfer['account'] = Account.objects.get(number=transfer['account'])
        except:
            raise ValueError(f"No bank account found for transfer:\n {transfer}")

        transfers.append(Transfer(**transfer))

    return transfers


# def main():
#     file_path = '/home/tom/Workspace/Projects-2/expenses/python/src/expense_tracker/fixtures/example_data.csv'
#     [transfer.save() for transfer in Transfer.transfers_from_csv(file_path)]
#
#
# if __name__ == "__main__":
#     main()