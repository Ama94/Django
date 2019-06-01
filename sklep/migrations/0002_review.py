# Generated by Django 2.2.1 on 2019-06-01 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklep', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sklep.Product')),
            ],
        ),
    ]
