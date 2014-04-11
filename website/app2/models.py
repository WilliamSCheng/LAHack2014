from django.db import models
# Create your models here.

class Stock(models.Model):
	# Automatically added on input
	date = models.DateTimeField(auto_now_add=True)

	symbol = models.CharField(max_length=10)
	shares = models.IntegerField()
	entering_price = models.IntegerField()

	# Fields that will be populated via API or webscraping
	exchange = models.CharField(max_length=20, null=True)
	current_price = models.IntegerField(null=True)
	current_volume = models.IntegerField(null=True)
	current_PE = models.IntegerField(null=True)
	current_PB = models.IntegerField(null=True)
	current_ROA = models.IntegerField(null=True)
	current_ROE = models.IntegerField(null=True)
	current_net_margin = models.IntegerField(null=True)
	current_rev_growth = models.IntegerField(null=True)
	current_dividend_yield = models.IntegerField(null=True)

	# Statistics on current vs difference
	current_difference = models.DecimalField(max_digits = 5, decimal_places = 2, null=True)
	current_difference_percentage = models.DecimalField(max_digits = 5, decimal_places = 2, null=True)
	

	def __unicode__(self):
		return str(self.date.isocalendar()) + ": " + str(self.shares) + " shares of the company " + self.symbol + " was bought at " + str(self.entering_price) + " dollars per share."

"""
Implement in the future
class Fund(models.Model):
	name = models.CharField(Max_length=100)
	stocks = models.ManyToManyField(Stock)
	total_value_under_management = models.IntegerField()

	def __unicode__(self):
		return "The " + self.name + " has " + str(total_value_under_management) + " dollars under management."
"""
