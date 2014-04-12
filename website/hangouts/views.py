from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Avg
from website.hangouts.models import Hangout

from django.contrib import messages

import urllib

data = {}

class HangoutListView(ListView):
	template_name = 'hangout_list.html'
	model = Hangout
