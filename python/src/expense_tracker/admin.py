from django.contrib import admin
from expense_tracker.models import Organization, Account, Transfer


# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "organization",)


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ("reference",

                    "account",
                    "recipient",

                    "amount",
                    "date",

                    "comment",)

    @staticmethod
    def account_to_name(obj):
        return obj.account_to.name
