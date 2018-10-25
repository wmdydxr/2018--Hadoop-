# Generated by Django 2.1.2 on 2018-10-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=20)),
                ('gdate', models.DateField()),
                ('gBoyNum', models.IntegerField()),
                ('gGrilNum', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sName', models.CharField(max_length=20)),
                ('sGender', models.BooleanField(default=True)),
                ('sAge', models.IntegerField()),
                ('sSummary', models.CharField(max_length=500)),
                ('sScore', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
                ('sClass', models.ForeignKey(on_delete=None, to='MyApp.Class')),
            ],
        ),
    ]
