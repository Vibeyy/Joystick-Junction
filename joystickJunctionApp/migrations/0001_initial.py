# Generated by Django 5.1.2 on 2024-10-27 14:18

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=30, verbose_name='Customer Name')),
                ('customerEmail', models.CharField(max_length=40, verbose_name='Email ID')),
                ('customerPhone', models.CharField(max_length=15, verbose_name='Phone No')),
                ('customerPassword', models.CharField(max_length=14, verbose_name='Password')),
                ('customerDateOfBirth', models.DateField(null=True)),
                ('customerGender', models.CharField(max_length=6, verbose_name='Gender')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productImage', models.ImageField(upload_to='productImages/', verbose_name='Product Image')),
                ('productName', models.CharField(max_length=50, verbose_name='Product Name')),
                ('productCategory', models.CharField(choices=[('Adventure', 'Adventure'), ('Sports', 'Sports'), ('Racing', 'Racing'), ('Shooting', 'Shooting')], max_length=40, verbose_name='Product Category')),
                ('productPrice', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Product Price')),
                ('productSellingPrice', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Product Selling Price')),
                ('productQuantity', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Product Quantity')),
                ('productDescription', models.TextField(verbose_name='Product Description')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAddressDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cutomerHouseNo', models.CharField(max_length=10, verbose_name='Customer House No')),
                ('cutomerAddressLine1', models.CharField(max_length=30, verbose_name='Address Line 1')),
                ('cutomerAddressLine2', models.CharField(max_length=30, verbose_name='Address Line 2')),
                ('customerCity', models.CharField(max_length=20, verbose_name='City')),
                ('customerState', models.CharField(max_length=20, verbose_name='State')),
                ('customerPinCode', models.IntegerField(verbose_name='Pin Code')),
                ('customerDeliveryNumber', models.CharField(max_length=15, verbose_name='Delivery Phone No')),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joystickJunctionApp.customerdetail')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokiyoOrderId', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='JJ Order Id')),
                ('deliverAddressInOrder', models.CharField(max_length=140, verbose_name='Delivery Address')),
                ('deliveryNumberInOrder', models.IntegerField(verbose_name='Delivery Phone No')),
                ('totalItemCostInOrder', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Total cost')),
                ('discountInOrder', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Discount')),
                ('totalAmountPaidInOrder', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Total amount paid')),
                ('orderPlacedTimeDate', models.CharField(default=None, max_length=30, verbose_name='order Placed Time & Date')),
                ('orderPlacedDate', models.DateField(default=django.utils.timezone.now, null=True)),
                ('orderDeliveredDate', models.DateField(default=django.utils.timezone.now, null=True)),
                ('orderStatusInOrder', models.CharField(default='N', max_length=1, verbose_name='Delivery Status')),
                ('customerIdInOrder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joystickJunctionApp.customerdetail')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetailsProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productQuantityInODP', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Quantity')),
                ('productPrizingInODP', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Sum of products')),
                ('customerIdInODP', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='joystickJunctionApp.customerdetail')),
                ('orderDetailSId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joystickJunctionApp.orderdetail')),
                ('productIdInODP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joystickJunctionApp.productdetail')),
            ],
        ),
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productQuantityInCart', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Quantity')),
                ('productPrizingInCart', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Sum of products')),
                ('customerIdInCart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joystickJunctionApp.customerdetail')),
                ('productIdInCart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='joystickJunctionApp.productdetail')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='productImages/', verbose_name='Product Image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='joystickJunctionApp.productdetail')),
            ],
        ),
    ]
