# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

def index(request):
    try:
        request.session['total_gold']
    except KeyError:
        request.session["total_gold"] = 0
    return render(request, 'ninjas/index.html')

def process_money(request, location):
    delta  = 0
    new = []
    action ='earned'
    if location == "farm":
        delta=random.randint(10, 21)
        new = {"message" : "Earned "+str(delta)+" golds from the "+location+"! "+datetime.strftime(datetime.today(), "(%Y/%m/%d %I:%M %p)"), "color" : "green"}
    elif location == "cave":
        delta=random.randint(5, 11)
        new = {"message" : "Earned "+str(delta)+" golds from the "+location+"! "+datetime.strftime(datetime.today(), "(%Y/%m/%d %I:%M %p)"), "color" : "green"}
    elif location == "house":
        delta=random.randint(2, 6)
        new = {"message" : "Earned "+str(delta)+" golds from the "+location+"! "+datetime.strftime(datetime.today(), "(%Y/%m/%d %I:%M %p)"), "color" : "green"}
    elif location == "casino":
        delta=random.randint(-50,50)
        if delta >= 0:
            new = {"message" : "Entered a casino and earned "+str(delta)+" golds! "+datetime.strftime(datetime.today(), "(%Y/%m/%d %I:%M %p)"), "color" : "green"}
        else:
            action = 'lost'
            new = {"message" : "Entered a casino and lost "+str(-delta)+" golds... Ouch... "+datetime.strftime(datetime.today(), "(%Y/%m/%d %I:%M %p)"), "color" : "red"}


    try:
        log_list = request.session['logs']
    except KeyError:
        log_list = []

    request.session['total_gold'] += delta

    log_list.append(new)
    request.session['logs'] = log_list
    return redirect("/")

def reset(request):
    request.session.clear()
    return redirect("/")
