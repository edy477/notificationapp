# Generated by Django 4.2.11 on 2024-04-06 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('SPORTS', 'Sports'), ('FINANCE', 'Finance'), ('MOVIES', 'Movies')], max_length=50),
        ),
        migrations.AlterField(
            model_name='notificationtype',
            name='name',
            field=models.CharField(choices=[('SMS', 'SMS'), ('EMAIL', 'Email'), ('PUSH_NOTIFICATION', 'Push Notification')], max_length=50),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
    ]