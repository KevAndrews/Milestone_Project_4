# Generated by Django 3.2.9 on 2022-01-01 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_product_game'),
        ('wishlists', '0002_auto_20220101_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='games_list',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.game'),
            preserve_default=False,
        ),
    ]
