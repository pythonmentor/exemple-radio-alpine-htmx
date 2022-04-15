from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from dateutil.relativedelta import relativedelta


class Password(models.Model):
    class Validity(models.IntegerChoices):
        SEMESTER = 6, _('six months')
        YEAR = 12, _("one year")

    password = models.CharField(_('password'), max_length=100, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='passwords',
    )
    created_date = models.DateTimeField(
        _('date of creation'),
        auto_now_add=True,
    )
    validity_period = models.IntegerField(
        _('password validity'),
        choices=Validity.choices,
        null=True,
        blank=True,
    )

    @property
    def expiration_date(self):
        """
        Expiration date of the password. None is not validity_period is defined.
        """
        if self.validity_period:
            return self.created_date + relativedelta(days=self.validity_period)
