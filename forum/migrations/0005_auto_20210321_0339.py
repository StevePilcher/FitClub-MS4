# Generated by Django 3.1.7 on 2021-03-21 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('forum', '0004_auto_20210321_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='originator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='profiles.userprofile'),
        ),
    ]