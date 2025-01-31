# Generated by Django 5.1.4 on 2025-01-06 08:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_alter_room_all_inclusive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='mysite.country'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_name', to='mysite.city'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_names', to='mysite.country'),
        ),
        migrations.AlterField(
            model_name='hotelphoto',
            name='hotel_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_images', to='mysite.hotel'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='hotel_reviews',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_ratings', to='mysite.hotel'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='stars',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_rooms', to='mysite.hotel'),
        ),
        migrations.AlterField(
            model_name='roomphoto',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_images', to='mysite.room'),
        ),
    ]
