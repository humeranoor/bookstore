# Generated by Django 3.2.4 on 2021-06-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pic',
            field=models.ImageField(default='no_picture.jpg', upload_to='books'),
        ),
    ]
