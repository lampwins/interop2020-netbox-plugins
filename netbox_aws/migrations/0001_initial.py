# Generated by Django 3.1 on 2020-09-14 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ipam', '0037_ipaddress_assignment'),
    ]

    operations = [
        migrations.CreateModel(
            name='VPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('container_prefix', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ipam.prefix')),
            ],
        ),
    ]
