from expense_tracker.models import Organization, Account, Transfer


def test_create_models(db):

    organization_tom = Organization.objects.create(name="Tom")
    assert organization_tom.name == "Tom"

    organization_jerry = Organization.objects.create(name="Jerry")
    assert organization_jerry.name == "Jerry"

    account_tom = Account.objects.create(number="BE00 0000 0000 000",
                                     name="Tom's account",
                                     organization=organization_tom)

    account_jerry = Account.objects.create(number="BE11 1111 1111 111",
                                           name="Jerry's account",
                                           organization=organization_jerry)

    transfer_1 = Transfer.objects.create(reference="xxx",
                                         account_from=account_tom,
                                         account_to=account_jerry,
                                         amount=999,
                                         currency="eur",
                                         date="2023-10-10",
                                         description="sepa",
                                         comment="test comment")

    assert transfer_1.reference == "xxx"
    assert transfer_1.account_from == account_tom

    account_anonymous = Account.objects.create(number="BE22 2222 2222 222",
                                               name="Anonymous' account")

    transfer_2 = Transfer.objects.create(reference="yyy",
                                         account_from=account_tom,
                                         account_to=account_anonymous,
                                         amount=999,
                                         currency="eur",
                                         date="2023-10-10",
                                         description="sepa",)

    assert transfer_2.reference == "yyy"
    assert transfer_2.account_from == account_tom


