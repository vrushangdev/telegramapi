from django.urls import path
from telegram import views

app_name = 'telegram'

urlpatterns = [
# Custom Operations & Procedures

    path('scrape-leads/', views.scrape_leads, name='scrape-leads'),
    path('send-message/', views.send_message, name='send-message'),
    path('scrape-admins/', views.scrape_admins, name='scrape-admins'),
    path('get-otp/', views.get_otp, name='get-otp'),
    path('verify-otp/', views.verify_otp, name='verify-otp'),

# Resources
    path('leads/', views.leads, name='leads'),
    path('campaigns/', views.campaigns, name='campaigns'),
    path('senders/', views.test, name='senders'),

]
