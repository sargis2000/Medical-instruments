# Generated by Django 4.0.4 on 2022-05-02 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Instruments', '0006_alter_partner_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banneritems',
            options={'verbose_name': 'Բանների լուսանկար', 'verbose_name_plural': 'Բանների լուսանկարներ'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Բաժին', 'verbose_name_plural': 'Բաժիններ'},
        ),
        migrations.AlterModelOptions(
            name='instrument',
            options={'verbose_name': 'Սարքավորում', 'verbose_name_plural': 'Սարքավորումներ'},
        ),
        migrations.AlterModelOptions(
            name='instrumentcontent',
            options={'verbose_name': 'Սարքավորում', 'verbose_name_plural': 'Սարքավորումներ'},
        ),
        migrations.AlterModelOptions(
            name='instrumentmodel',
            options={'verbose_name': 'Սարքավորման մոդել', 'verbose_name_plural': 'Սարքավորման մոդեներ'},
        ),
        migrations.AlterModelOptions(
            name='modelcontent',
            options={'verbose_name': 'Մոդել կոնտենտ', 'verbose_name_plural': 'Մոդել կոնտենտներ'},
        ),
    ]
