# Generated by Django 4.1.5 on 2023-01-07 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_calls_video_username_alter_posts_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='file',
            field=models.FileField(null=True, upload_to='frontend/src/post_images'),
        ),
        migrations.AlterField(
            model_name='status_model',
            name='status',
            field=models.FileField(null=True, upload_to='frontend/src/post_images'),
        ),
    ]
