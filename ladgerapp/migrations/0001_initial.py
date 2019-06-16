# Generated by Django 2.2.2 on 2019-06-14 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laddger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Particulars', models.CharField(max_length=50)),
                ('Debit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Credit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('Accounthead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ladgerapp.Laddger')),
            ],
        ),
    ]