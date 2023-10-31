from expense_tracker.models import Organization, Account, Transfer


def test_create_models(db):

    organization_tom = Organization.objects.create(name="Tom")
    assert Organization.objects.get(name="Tom").name == "Tom"

    account_tom = Account.objects.create(number="BE00 0000 0000 000",
                                         name="Tom's account",
                                         organization=organization_tom)
    assert Account.objects.get(name="Tom's account").number == "BE00 0000 0000 000"

    transfer = Transfer.objects.create(reference="xxx",
                                       account=account_tom,
                                       recipient="BE11 1111 1111 111",
                                       amount=999,
                                       date="2023-10-10",
                                       comment="some comment")
    assert Transfer.objects.get(reference="xxx").amount == 999
