# Generated by Django 3.0.7 on 2020-09-03 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('title', models.CharField(max_length=60)),
                ('author', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=60)),
                ('urlname', models.SlugField()),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('content', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(editable=False)),
                ('updated_at', models.DateTimeField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Post')),
            ],
        ),
    ]