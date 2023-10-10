from django.contrib import admin
from expense_tracker.models import Organization, Account, Transfer


# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    pass
