# Generated by Django 3.2.4 on 2021-07-02 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingprofile',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
