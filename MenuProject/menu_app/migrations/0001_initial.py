# Generated by Django 4.1.4 on 2022-12-22 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField(default=0)),
                ('is_special', models.BooleanField(default=False)),
                ('is_vegan', models.BooleanField(default=False)),
                ('is_publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('food', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu_app.food')),
            ],
        ),
    ]
