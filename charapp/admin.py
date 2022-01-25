from django.contrib import messages,admin
from django.utils.translation import ngettext

from .models import donation_request

# Register your models here.
class DonationAdmin(admin.ModelAdmin):
    list_display = ['donation_amount', 'status']
    ordering = ['donation_amount']
    actions = ['make_approval','make_rejection']

    @admin.action(description='Approve')
    def make_approval(self, request, queryset):
        updated = queryset.update(status='A')
        self.message_user(request, ngettext(
            '%d Donation was successfully approved.',
            '%d Donations were successfully approved.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Withdraw')
    def make_rejection(self, request, queryset):
        updated = queryset.update(status='w')
        self.message_user(request, ngettext(
            '%d Donation withdrawn.',
            '%d Donations withdrawn.',
            updated,
        ) % updated, messages.SUCCESS)

admin.site.register(donation_request, DonationAdmin)
