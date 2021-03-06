# Generated by Django 3.0.7 on 2020-06-28 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_punter_field_is_nullable'),
    ]

    operations = [
        migrations.AddField(
            model_name='pun',
            name='run',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.Run', verbose_name='Pun Run'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pun',
            name='punter',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Punter', verbose_name='Punter'),
        ),
    ]
