from django.db import models
from django.urls import reverse
from utilities.querysets import RestrictedQuerySet

from netbox_aws.choices import VPCRegionChoices


class VPC(models.Model):
    created = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=True
    )
    name = models.CharField(
        max_length=255
    )
    slug = models.SlugField()
    description = models.CharField(
        max_length=255
    )
    container_prefix = models.ForeignKey(
        to="ipam.Prefix",
        on_delete=models.PROTECT
    )
    region = models.CharField(
        max_length=255,
        choices=VPCRegionChoices
    )

    objects = RestrictedQuerySet.as_manager()

    class Meta:
        verbose_name = 'VPC'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_aws:vpc", args=[self.slug])
