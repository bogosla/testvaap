from django.db import models



class Product(models.Model):
	M = "M"
	F = "F"
	U = "U"

	GENDERS = (
		(M, 'M'),
		(F, 'F'),
		(U, 'U')
	)

	product = models.CharField(max_length=60, unique=True)
	purchase = models.FloatField(default=0.0)
	sale = models.FloatField(default=0.0)
	qty = models.PositiveIntegerField(default=10)
	gender = models.CharField(max_length=1, default=M, choices=GENDERS)
	note = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product