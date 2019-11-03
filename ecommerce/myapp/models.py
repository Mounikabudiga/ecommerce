from django.db import models


# Create your models here.
class product_field(models.Model):
	name = models.CharField(max_length = 25)
	description = models.CharField(max_length = 25)
	cost = models.IntegerField()
	noofproducts= models.CharField(max_length = 25)
	


	def __str__(self):
		return self.name


class user_field(models.Model):
	username = models.CharField(max_length = 25)
	phone_no = models.CharField(max_length = 25)
	email = models.CharField(max_length = 25)
	account_bln = models.IntegerField()

	def __str__(self):
		return self.username

class buyer(models.Model):
	user=models.ForeignKey(user_field,on_delete=models.CASCADE)
	product=models.ForeignKey(product_field,on_delete=models.CASCADE)

	def __str__(self):
		return "{}----{}".format(self.product,self.user)