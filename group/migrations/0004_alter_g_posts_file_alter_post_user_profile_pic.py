# Generated by Django 4.1.5 on 2023-01-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_alter_g_posts_file_alter_post_user_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='g_posts',
            name='file',
            field=models.FileField(null=True, upload_to='frontend/src/post_images'),
        ),
        migrations.AlterField(
            model_name='post_user',
            name='profile_pic',
            field=models.FileField(null=True, upload_to='frontend/src/post_images'),
        ),
    ]
