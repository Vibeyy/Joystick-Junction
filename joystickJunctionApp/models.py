from typing import Any
from django.db import models
from django.utils import timezone

class CustomerDetail(models.Model):
    customerName = models.CharField('Customer Name', max_length=30)
    customerEmail = models.CharField('Email ID', max_length=40)
    customerPhone = models.CharField('Phone No', max_length=15)
    customerPassword = models.CharField('Password', max_length=14)
    customerDateOfBirth = models.DateField(null=True)
    customerGender = models.CharField('Gender', max_length=6)
    
    def __str__(self):
        return f"The Customer : {self.customerName}"

class CustomerAddressDetail(models.Model):
    customerId = models.ForeignKey(CustomerDetail, on_delete=models.CASCADE)
    cutomerHouseNo = models.CharField('Customer House No', max_length=10)
    cutomerAddressLine1  = models.CharField('Address Line 1', max_length=30)
    cutomerAddressLine2  = models.CharField('Address Line 2', max_length=30)
    customerCity = models.CharField('City', max_length=20)
    customerState = models.CharField('State', max_length=20)
    customerPinCode = models.IntegerField('Pin Code')
    customerDeliveryNumber = models.CharField('Delivery Phone No', max_length=15)
    
    def __str__(self):
        return f"Address Id {self.customerId.customerName}"


class ProductDetail(models.Model):

    CATEGORY_CHOICES = [
        ('PARTIALLY PHYSICAL', 'PARTIALLY PHYSICAL'),
        ('SENSORY', 'SENSORY'),
        ('INTELLECTUAL', 'INTELLECTUAL'),
        ('MENTAL HEALTH AND EMOTIONAL', 'MENTAL HEALTH AND EMOTIONAL'),
    ]
   
    productImage = models.ImageField("Product Image", upload_to='productImages/')
    productName = models.CharField('Product Name', max_length=50)
    productCategory = models.CharField('Product Category', max_length=40, choices=CATEGORY_CHOICES)
    productPrice = models.DecimalField('Product Price', max_digits=7, decimal_places=2)
    productSellingPrice = models.DecimalField('Product Selling Price', max_digits=7, decimal_places=2)
    productQuantity = models.DecimalField('Product Quantity', max_digits=5, decimal_places=2)
    productDescription = models.TextField('Product Description')


    def __str__(self):
        return f"The : {self.productName} {self.id}"

class ProductImage(models.Model):
    product = models.ForeignKey(ProductDetail, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField("Product Image", upload_to='productImages/')
    
    def __str__(self):
        return f"Image for {self.product.productName}"

class CartDetail(models.Model):
    customerIdInCart = models.ForeignKey(CustomerDetail, to_field='id', on_delete=models.CASCADE)
    productIdInCart = models.ForeignKey(ProductDetail,to_field='id', on_delete=models.CASCADE)
    productQuantityInCart = models.DecimalField("Quantity", max_digits=3, decimal_places=0)
    productPrizingInCart = models.DecimalField("Sum of products", max_digits=10, decimal_places=2,default=0.0)

    def __str__(self):
        return f"Card {self.id}"
    
class OrderDetail(models.Model):
    customerIdInOrder = models.ForeignKey(CustomerDetail, to_field='id', on_delete=models.CASCADE)
    tokiyoOrderId = models.DecimalField('JJ Order Id',  max_digits=9, decimal_places=0) # 369000001
    deliverAddressInOrder = models.CharField('Delivery Address', max_length=140)
    deliveryNumberInOrder = models.IntegerField('Delivery Phone No')
    totalItemCostInOrder = models.DecimalField('Total cost', max_digits=9, decimal_places=2)
    discountInOrder = models.DecimalField('Discount', max_digits=9, decimal_places=2)
    totalAmountPaidInOrder = models.DecimalField('Total amount paid', max_digits=9, decimal_places=2)
    orderPlacedTimeDate = models.CharField('order Placed Time & Date', max_length=30,default=None)
    orderPlacedDate = models.DateField(null=True,default=timezone.now)
    orderDeliveredDate = models.DateField(null=True,default=timezone.now)
    orderStatusInOrder = models.CharField('Delivery Status', max_length=1,default='N')

    def __str__(self):
        return f"Order :{self.tokiyoOrderId}"
    
class OrderDetailsProduct(models.Model):
    customerIdInODP = models.ForeignKey(CustomerDetail, to_field='id', on_delete=models.CASCADE,default=None)
    orderDetailSId = models.ForeignKey(OrderDetail, to_field='id', on_delete=models.CASCADE)
    productIdInODP = models.ForeignKey(ProductDetail,to_field='id', on_delete=models.CASCADE)
    productQuantityInODP = models.DecimalField("Quantity", max_digits=3, decimal_places=0)
    productPrizingInODP = models.DecimalField("Sum of products", max_digits=10, decimal_places=2,default=0.0)

    def __str__(self):
        return f"order details {self.id}_{self.productIdInODP.productName}"
