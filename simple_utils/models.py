from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.util import timezone

class BaseModel(SelfAwareModel):
    updated = models.DateTimeField()
    created = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created = timezone.now()
        
        self.updated = timezone.now()

        return super(BaseModel, self).save(*args, **kwargs)

class SelfAwareModel(models.Model):
    def get_ct(self):
        return ContentType.objects.get_for_model(self)

    def get_ct_id(self):
        return self.get_ct().pk

    def get_app_label(self):
        return self.get_ct().app_label

    def get_model_name(self):
        return self.get_ct().model

    class Meta:
        abstract = True


class ReadOnlyModel(models.Model):
    def save(self, *args, **kwargs):
        return

    def delete(self, *args, **kwargs):
        return

    class Meta:
        abstract = True
