from django.db import models
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from django.http import Http404

from polls.models import Poll

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	# output = ', '.join([p.question for p in latest_poll_list])
	template = loader.get_template('polls/index.html')
	context = {'latest_poll_list': latest_poll_list}
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)