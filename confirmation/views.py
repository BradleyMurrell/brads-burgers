from django.shortcuts import render
from .models import Order
from django.views.decorators.csrf import csrf_exempt
import random
import json


def randomOrderNumber(length):
    sample = 'ABCDEFGH0123456789'
    numberO = ''.join((random.choice(sample) for i in range(length)))
    return numberO


@csrf_exempt
def confirmation(request):
    request.session.set_expiry(0)
    if request.is_ajax():
        request.session['orders'] = request.POST.get('orders')
        order = json.loads(request.session['orders'])
        request.session['total'] = request.POST.get('total')
        if request.user.is_authenticated:
            order = Order(number=randomOrderNumber(3), name=order, total=float(request.session['total']))
            order.save()
    return render(request, 'confirmation/confirmation.html')


def success(request):
    order = request.session['orders']
    ctx = {'order': order}
    return render(request, 'confirmation/success.html', ctx)
