import imp
from django.db import models
import uuid
from fileapp.constant import create_slug
# Create your models here.

class ToolFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=511)
    image = models.ImageField(max_length=255, upload_to='WOWPDF/icons', null=True, blank=True)
    rank = models.IntegerField(default=0, null=True, blank=True)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            slugs = list(ToolFile.objects.all().values_list('slug', flat=True))
            self.slug = create_slug(name=self.name, slugs=slugs)
        super(ToolFile, self).save(*args, **kwargs)

    class Meta:
        db_table = 'ToolFile'

    def __str__(self):
        return str(self.name)
    
class WowFiles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    file1 = models.FileField(upload_to='WOWPDF/files/%Y/%m',null=True, blank=True)
    file2 = models.FileField(upload_to='WOWPDF/files/%Y/%m',null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_compressed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table='WowFiles'
