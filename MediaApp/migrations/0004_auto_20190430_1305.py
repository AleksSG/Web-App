# Generated by Django 2.2 on 2019-04-30 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MediaApp', '0003_auto_20190409_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MediaApp.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MediaApp.UserProfileInfo')),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]