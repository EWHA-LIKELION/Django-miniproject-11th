# Generated by Django 4.2 on 2023-05-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_hashtag_blog_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='blog_photo'),
        ),
    ]
