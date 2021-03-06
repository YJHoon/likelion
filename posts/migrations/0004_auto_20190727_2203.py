# Generated by Django 2.2.3 on 2019-07-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='ingredient',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='level',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
