# Generated by Django 2.2 on 2020-07-01 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legaltec', '0002_delete_aseguradora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aseguradora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aseguradora', models.CharField(max_length=120, verbose_name='Aseguradora')),
            ],
            options={
                'verbose_name_plural': 'Aseguradoras',
            },
        ),
    ]
