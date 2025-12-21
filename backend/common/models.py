import uuid

from autoslug import AutoSlugField

from dirtyfields import DirtyFieldsMixin

from django.db import models

from common.helpers.slugs import get_slug


class BaseModel(DirtyFieldsMixin, models.Model):
    uid = models.UUIDField(
        db_index=True, unique=True, default=uuid.uuid4, editable=False
    )
    slug = AutoSlugField(populate_from=get_slug, unique=True, db_index=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_at",)
