# Generated by Django 3.2.13 on 2022-11-30 00:51

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20221129_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_img',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
