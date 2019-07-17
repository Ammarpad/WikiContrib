# Generated by Django 2.2.2 on 2019-07-11 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('query', '0010_auto_20190711_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListCommit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('platform', models.CharField(choices=[('pb', 'Phabricator'), ('gr', 'Gerrit'), ('gt', 'Git')], max_length=2)),
                ('created_on', models.DateTimeField()),
                ('redirect', models.CharField(max_length=200)),
                ('query', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='query.Query')),
            ],
        ),
    ]