from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from retrosnacks.views import (
    index, contact, formules, offerte, snackssauzen, faq, voorwaarden, 
    login_page, login_view, privacy, dashboard_view, logout_view, 
    offertes_view, facturen_view, offerte_aanpassen, save_offerte, 
    create_client_eenvoudigfactureren, delete_offerte, export_offerte_to_docx, event, invoice_list, offertes_overzicht, get_offerte_details, klanten_view, update_offerte_status, klant_aanpassen, zelf_offerte, klant_aanpassen, geplande_feesten, klant_verwijderen, kalender_events, export_klanten_excel, ActieListView, acties_overzicht
)

urlpatterns = [
    path('', index, name='index'),
    path('formules/', formules, name='formules'),
    path('offerte/', offerte, name='offerte'),
    path('snackssauzen/', snackssauzen, name='SnacksSauzen'),  
    path('faq/', faq, name='faq'),  
    path('voorwaarden/', voorwaarden, name='voorwaarden'),
    path('login/', login_page, name='login'),
    path('login/auth/', login_view, name='login_view'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
    path('privacy/', privacy, name='privacy'),
    path('event/', event, name='event'),
    path('contact/', contact, name='contact'),
    path('klant_aanpassen/', klant_aanpassen, name='klant_aanpassen'),
    path('zelf_offerte/', zelf_offerte, name='zelf_offerte'),
   
    
    # Offertes en facturen
    path('offertes/', offertes_view, name='offertes'),
    path('delete_offerte/', delete_offerte, name='delete_offerte'),
    path('facturen/', invoice_list, name='facturen'),  # Gebruik invoice_list voor facturen
    path('klanten/', klanten_view, name='klanten'),

    path('offerte_aanpassen/<int:offerte_id>/', offerte_aanpassen, name='offerte_aanpassen'),
    path('offertes/', offertes_overzicht, name='offertes_overzicht'),  

    path('save_offerte/', save_offerte, name='save_offerte'),
    path('create_client_eenvoudigfactureren/', create_client_eenvoudigfactureren, name='create_client_eenvoudigfactureren'),
    path('export_offerte_docx/<int:offerte_id>/', export_offerte_to_docx, name='export_offerte_docx'),
    path('get-offerte-details/<int:offerte_id>/', get_offerte_details, name='get_offerte_details'),
    path('update-offerte-status/<int:offerte_id>/', update_offerte_status, name='update_offerte_status'),
    path('klant_aanpassen/<int:klant_id>/', klant_aanpassen, name='klant_aanpassen'),
    path('klant/verwijderen/<int:klant_id>/', klant_verwijderen, name='klant_verwijderen'),


    path('geplande-feesten/', geplande_feesten, name='geplande_feesten'),

    path('api/kalender-events/', kalender_events, name='kalender_events'),

    path('klanten/export-excel/', export_klanten_excel, name='export_klanten_excel'),

    path('acties/', ActieListView.as_view(), name='actie_list'),
    path('acties/', acties_overzicht, name='acties_overzicht'),





    

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)