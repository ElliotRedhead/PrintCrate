from django.db import models

class product(models.Model):
	product_name=models.CharField(max_length=100)

	def __str__(self):
		return self.product_name
