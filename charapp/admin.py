from django.contrib import messages,admin
from django.utils.translation import ngettext
from .models import NGO, donation_request , Profile, Category

# Register your models here.
admin.site.register(Profile)
admin.site.register(NGO)
admin.site.register(donation_request)
admin.site.register(Category)


class DonationAdmin(admin.ModelAdmin):
    list_display = ['ngo_name','status']
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

