# Generated by Django 3.2.2 on 2021-05-29 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='namePD',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='prices',
        ),
        migrations.AddField(
            model_name='product',
            name='amounts',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='body',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='typePD',
            field=models.CharField(blank=True, choices=[('CPU', 'Cpu'), ('Mainboard', 'Mainboard'), ('RAM', 'Ram'), ('VGA', 'Vga')], max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='urlsPD',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='store.product')),
            ],
        ),
    ]