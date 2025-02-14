# Generated by Django 4.1.3 on 2022-11-22 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wiki', '0012_auto_20200629_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='related_documents',
            field=models.ManyToManyField(blank=True, to='wiki.document'),
        ),
        migrations.AlterField(
            model_name='draftrevision',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='draftrevision',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='wiki.document'),
        ),
        migrations.AlterField(
            model_name='revision',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_%(class)ss', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='revision',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to='wiki.document'),
        ),
    ]
