
from django import forms
from .models import ActieVanHetMoment


class ActieForm(forms.ModelForm):
    actief_tot = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Geldig tot"
    )
    

    class Meta:
        model = ActieVanHetMoment
        fields = ['titel', 'omschrijving', 'actief_tot']
        widgets = {
            'titel': forms.TextInput(attrs={'class': 'form-control'}),
            'omschrijving': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}), # Hier is de aanpassing!
            'actief_tot': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), # Of DateTimeInput afhankelijk van je model
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)





class CateringRequestForm(forms.Form):
    name = forms.CharField(label='Naam', max_length=100, required=True)
    company = forms.CharField(label='Bedrijf/Organisatie', max_length=100, required=False)
    email = forms.EmailField(label='E-mail', required=True)
    phone = forms.CharField(label='Telefoonnummer', max_length=20, required=True)
    event_name = forms.CharField(label='Naam event', max_length=100, required=False)
    event_date = forms.DateField(label='Datum Evenement', required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    visitors = forms.ChoiceField(
        label='Verwacht Aantal Bezoekers',
        choices=[
            ('', 'Selecteer aantal bezoekers'),
            ('500-1000', '500-1000 bezoekers'),
            ('1000-2500', '1000-2500 bezoekers'),
            ('2500+', 'Meer dan 2500 bezoekers'),
        ],
        required=True
    )
    foodtrucks = forms.MultipleChoiceField(
        label='Gewenste Foodtruck(s)',
        choices=[
            ('frietwagen', 'Frietwagen'),
            ('hamburgerkraam', 'Hamburgerkraam'),
            ('pastakraam', 'Pastakraam'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    extra_info = forms.CharField(
        label='Extra Informatie en Wensen',
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Deel hier uw specifieke wensen of aanvullende informatie...'}),
        required=False
    )


class OfferteForm(forms.Form):
    naam_contactpersoon = forms.CharField(max_length=100)
    email = forms.EmailField()
    aantal_personen = forms.IntegerField(min_value=1)
    straat = forms.CharField(max_length=100)
    nummer = forms.CharField(max_length=20)
    gemeente = forms.CharField(max_length=100)
    telefoon = forms.CharField(max_length=20)
    gewenste_datum = forms.DateField(input_formats=['%Y-%m-%d'])
    gewenste_tijd = forms.CharField(max_length=5)  # bv. '14:30'
    formule = forms.CharField(max_length=100)

    # optionele velden
    extra_info = forms.CharField(required=False, max_length=500)
    naam_bedrijf = forms.CharField(required=False, max_length=100)
    btw = forms.CharField(required=False, max_length=50)
    afstand = forms.DecimalField(required=False, max_digits=6, decimal_places=2)
    extra_kosten = forms.DecimalField(required=False, max_digits=10, decimal_places=2)
    basis_prijs = forms.DecimalField(required=False, max_digits=10, decimal_places=2)
    totaal_prijs = forms.DecimalField(required=False, max_digits=10, decimal_places=2)
    korting = forms.DecimalField(required=False, max_digits=6, decimal_places=2)
