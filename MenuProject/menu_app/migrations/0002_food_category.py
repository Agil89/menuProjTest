# Generated by Django 4.1.4 on 2022-12-22 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_category', to='menu_app.foodcategory'),
            preserve_default=False,
        ),
    ]
