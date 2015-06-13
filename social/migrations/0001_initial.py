# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('link', models.URLField()),
                ('join_string', models.CharField(help_text=b'Used when the Provider is concatenated onto something.', max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
