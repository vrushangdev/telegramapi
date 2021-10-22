from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def test(request):
    return HttpResponse("TEST")

# Custom Operations & Procedures

def scrape_leads(request):
    return HttpResponse("Scrape Leads **Pending")

def send_message(request):
    return HttpResponse("Send Message **Pending")

def get_otp(request):
    """
    Generate 6 Digit Number & Send It Via Mail & Phone Number
    :param request:
    :return:
    """
    return HttpResponse("Get OTP **Pending")

def verify_otp(request):
    """
    Generate 6 Digit Number & Send It Via Mail & Phone Number
    :param request:
    :return:
    """
    return HttpResponse("Verify OTP **Pending")

def scrape_admins(request):
    return HttpResponse("Scrape Admins **Pending")

# Resources

def leads(request):
    return HttpResponse("Replace With Rest Frame Work View **Pending")

def campaigns(request):
    return HttpResponse("Replace With Rest Frame Work View **Pending")

def senders(request):
    return HttpResponse("Replace With Rest Frame Work View **Pending")