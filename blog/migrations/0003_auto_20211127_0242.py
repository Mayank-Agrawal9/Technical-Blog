# Generated by Django 3.2.2 on 2021-11-26 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
    ]
