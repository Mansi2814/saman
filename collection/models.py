from django.db import models
from datetime import timedelta, date
import datetime

# Create your models here.

class Men(models.Model):
    product_id=models.CharField(max_length=20, primary_key=True)
    category=models.CharField(max_length=122)
    name=models.CharField(max_length=50)
    Price=models.CharField(max_length=100)
    product_img=models.ImageField(null=True, upload_to="collection/images")
    addedToCart=models.BooleanField(default=False)
    quantity=models.IntegerField(default=1)
    latest=models.BooleanField(default=False)
    featured=models.BooleanField(default=False)
    desc=models.CharField(max_length=1000, default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi neque temporibus labore magni voluptate! Deleniti impedit maiores dolor sit corporis placeat perferendis, illum molestias mollitia deserunt nesciunt distinctio")
    quantity_ordered=models.IntegerField(default=1)
    ordered_on=models.DateField(default=datetime.date.today)
    deliverd=models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)
    delivered_on=models.DateField(default=date.today() + timedelta(days=10))
    expected_delivery=models.DateField(default=date.today() + timedelta(days=10))
    mop=models.CharField(max_length=20,default="COD")

    def added(self):
        self.addedToCart=True
        self.save()
        print("added")

    def deleted(self):
        self.addedToCart=False
        self.quantity=1
        self.save()
        print("deleted")

    def changedQuantity(self,quan):
        self.quantity=quan
        self.save()

    def ordered1(self):
        self.ordered=True
        self.save()

    def change_quantity_ordered(self):
        self.quantity_ordered=self.quantity
        self.save()



class Women(models.Model):
    product_id=models.CharField(max_length=20, primary_key=True)
    category=models.CharField(max_length=122)
    name=models.CharField(max_length=50)
    Price=models.CharField(max_length=100)
    product_img=models.ImageField(null=True, upload_to="collection/images")
    addedToCart=models.BooleanField(default=False)
    quantity=models.IntegerField(default=1)
    latest=models.BooleanField(default=False)
    featured=models.BooleanField(default=False)
    desc = models.CharField(max_length=1000,default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi neque temporibus labore magni voluptate! Deleniti impedit maiores dolor sit corporis placeat perferendis, illum molestias mollitia deserunt nesciunt distinctio")
    quantity_ordered=models.IntegerField(default=1)
    ordered_on=models.DateField(default=datetime.date.today)
    deliverd=models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)
    delivered_on=models.DateField(default=date.today() + timedelta(days=10))
    expected_delivery=models.DateField(default=date.today() + timedelta(days=10))
    mop=models.CharField(max_length=20,default="COD")


    def added(self):
        self.addedToCart=True
        self.save()
        print("added")

    def deleted(self):
        self.addedToCart=False
        self.quantity=1
        self.save()
        print("deleted")

    def changedQuantity(self,quan):
        self.quantity=quan
        self.save()

    def ordered1(self):
        self.ordered = True
        self.save()

    def change_quantity_ordered(self):
        self.quantity_ordered = self.quantity
        self.save()



class Accessory(models.Model):
    product_id=models.CharField(max_length=20, primary_key=True)
    category=models.CharField(max_length=122)
    name=models.CharField(max_length=50)
    Price=models.CharField(max_length=100)
    product_img=models.ImageField(null=True, upload_to="collection/images")
    addedToCart=models.BooleanField(default=False)
    quantity=models.IntegerField(default=1)
    latest=models.BooleanField(default=False)
    featured=models.BooleanField(default=False)
    desc = models.CharField(max_length=1000,default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi neque temporibus labore magni voluptate! Deleniti impedit maiores dolor sit corporis placeat perferendis, illum molestias mollitia deserunt nesciunt distinctio")
    quantity_ordered=models.IntegerField(default=1)
    ordered_on=models.DateField(default=datetime.date.today)
    deliverd=models.BooleanField(default=False)
    ordered = models.BooleanField(default=False)
    delivered_on=models.DateField(default=date.today() + timedelta(days=10))
    expected_delivery=models.DateField(default=date.today() + timedelta(days=10))
    mop=models.CharField(max_length=20,default="COD")

    def added(self):
        self.addedToCart=True
        self.save()
        print("added")

    def deleted(self):
        self.addedToCart=False
        self.quantity=1
        self.save()
        print("deleted")

    def changedQuantity(self,quan):
        self.quantity=quan
        self.save()

    def ordered1(self):
        self.ordered = True
        self.save()

    def change_quantity_ordered(self):
        self.quantity_ordered = self.quantity
        self.save()


# class Orders(models.Model):
#     product_id=models.CharField(max_length=20, primary_key=True)
#     quantity_ordered=models.IntegerField(default=1)
#     ordered_on=models.DateField(default=datetime.date.today)
#     deliverd=models.BooleanField(default=False)
#     delivered_on=models.DateField(default=date.today() + timedelta(days=10))
#     expected_delivery=models.DateField(default=date.today() + timedelta(days=10))
#     mop=models.CharField(max_length=20,default="COD")




