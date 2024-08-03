# Generated by Django 5.0.4 on 2024-06-24 21:05

from django.db import migrations


def set_rarity(apps, schema_editor):
    Item = apps.get_model('main_app', 'Item')
    all_items = Item.objects.all()

    for item in all_items:
        if item.price <= 10:
            item.rarity = 'Rare'
        elif item.price <= 20:
            item.rarity = 'Very Rare'
        elif item.price <= 30:
            item.rarity = 'Extremely Rare'
        else:
            item.rarity = 'Mega Rare'

    Item.objects.bulk_update(all_items, ['rarity'])


def remove_item_rarity(apps, schema_editor):
    Item = apps.get_model('main_app', 'Item')
    all_items = Item.objects.all()

    for item in all_items:
        item.rarity = Item._meta.get_field('rarity').default

    Item.objects.bulk_update(all_items, ['rarity'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_item'),
    ]

    operations = [migrations.RunPython(set_rarity, remove_item_rarity)
    ]