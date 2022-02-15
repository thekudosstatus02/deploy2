# Generated by Django 3.1.7 on 2021-06-07 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dp', models.ImageField(max_length=200, upload_to='images/')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=200)),
                ('dept', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('education', models.CharField(blank=True, max_length=200)),
                ('guide', models.TextField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=20)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anne.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=200)),
                ('unit_imp', models.TextField(blank=True, max_length=1000)),
                ('unit_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anne.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_date', models.DateTimeField(auto_now=True)),
                ('topic_name', models.CharField(max_length=200)),
                ('topic_weightage', models.TextField(blank=True, max_length=1000)),
                ('unit_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anne.unit')),
            ],
            options={
                'ordering': ['-topic_date'],
            },
        ),
    ]
