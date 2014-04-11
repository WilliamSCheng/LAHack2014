from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Avg
from website.fund_tracker.models import Stock

from django.contrib import messages

import urllib

data = {}

def __request(symbol, stat):
	url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (symbol, stat)
	return urllib.urlopen(url).read().strip().strip('"')

def get_stock_info(symbol):
	values = __request(symbol, 'l1rp6vx').split(',')
	data['price'] = values[0]
	data['price_earnings_ratio'] = values[1]
	data['price_book_ratio'] = values[2]
	data['volume'] = values[3]
	data['stock_exchange'] = values[4]

class StockListView(ListView):
	template_name = 'stock_list.html'
	model = Stock

	def get_context_data(self, **kwargs):
		context = super(StockListView, self).get_context_data(**kwargs)
		for stock in context['stock_list']:
			get_stock_info(stock.symbol)
			stock.exchange = data['stock_exchange']
			stock.current_price = data['price']
			stock.current_PE = data['price_earnings_ratio']
			stock.current_PB = data['price_book_ratio']
			stock.volume = data['volume']
			stock.current_difference = (float(stock.current_price) - float(stock.entering_price)) * float(stock.shares)
			stock.current_difference_percentage = round(float(stock.current_price) / float(stock.entering_price), 2)
		return context
