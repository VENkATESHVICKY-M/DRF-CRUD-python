# Generated by Django 3.2.4 on 2021-06-24 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210624_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=105)),
                ('lastname', models.CharField(max_length=105)),
                ('fullname', models.CharField(max_length=210)),
                ('countryid', models.IntegerField()),
                ('phonenumber', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='phoneprimary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='phonesecondary',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='postalcode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.users'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]