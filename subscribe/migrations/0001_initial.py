# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 08:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribed', to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set([('user', 'content_type', 'object_id')]),
        ),
    ]
