# Generated by Django 3.0.8 on 2020-07-28 09:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authprofiles', '0003_auto_20200727_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='PassportAPI',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('identifier', models.CharField(max_length=140)),
                ('name', models.CharField(max_length=140)),
            ],
        ),
        migrations.AddField(
            model_name='passportapplication',
            name='audience',
            field=models.ManyToManyField(related_name='application_audience', to='authprofiles.PassportAPI'),
        ),
    ]
