# Generated by Django 4.1.4 on 2024-05-07 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiments', '0015_experiment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experimentexecution',
            name='user_name',
        ),
        migrations.AddField(
            model_name='experiment',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='experiments', to='experiments.project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='experimentexecution',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experimentexecutions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experiment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experiments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='experimentexecution',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experimentexecutions', to='experiments.project'),
        ),
    ]
