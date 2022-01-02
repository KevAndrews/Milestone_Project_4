# Generated by Django 3.2.9 on 2022-01-01 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_product_game'),
        ('wishlists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='game',
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='games_list',
            field=models.ManyToManyField(related_name='games', to='products.Game'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='title',
            field=models.CharField(default='Wishlist 1', max_length=50),
        ),
    ]