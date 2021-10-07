from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects.all().order_by('-id')

    return render(request, "portfolio/portfolio.html", {'portafolios':portfolios})