# Generated by Django 4.2 on 2023-04-14 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_author_email_alter_post_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='post'),
        ),
    ]
