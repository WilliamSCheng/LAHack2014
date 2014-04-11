from django.contrib import admin
from website.fund_tracker.models import Stock

class StockAdmin(admin.ModelAdmin):
	readonly_fields = ['exchange', 'current_price', 'current_volume', 'current_PE', 'current_PB', 'current_ROA', \
					  'current_ROE', 'current_net_margin', 'current_rev_growth', \
					  'current_dividend_yield', 'current_difference_percentage', 'current_difference']
admin.site.register(Stock, StockAdmin)
