import datetime
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

# Zorg ervoor dat 'retrosnacks' de correcte naam van je app is
# waarin het Offerte model zich bevindt.
from retrosnacks.models import Offerte

class Command(BaseCommand):
    help = 'Verstuurt platte tekst herinneringsmails voor evenementen die over 7 dagen plaatsvinden.'

    def handle(self, *args, **options):
        vandaag = timezone.now().date()
        datum_voor_herinnering = vandaag + datetime.timedelta(days=7)

        self.stdout.write(self.style.NOTICE(
            f"Script gestart op {timezone.now().strftime('%Y-%m-%d %H:%M:%S')}."
        ))
        self.stdout.write(self.style.NOTICE(
            f"Zoeken naar offertes voor herinneringen op datum: {datum_voor_herinnering.strftime('%Y-%m-%d')}."
        ))

        # Filter offertes:
        # - Status is "Feest ingepland"
        # - Gewenste datum is precies 7 dagen vanaf vandaag
        # - Er is nog geen herinnering verstuurd (herinnering_verstuurd_op is leeg/null)
        offertes_voor_herinnering = Offerte.objects.filter(
            is_bevestigd="Feest ingepland",
            gewenste_datum=datum_voor_herinnering,
            herinnering_verstuurd_op__isnull=True  # Belangrijk om dubbele mails te voorkomen
        )

        if not offertes_voor_herinnering.exists():
            self.stdout.write(self.style.SUCCESS(
                f'Geen offertes gevonden om een herinnering voor te sturen voor {datum_voor_herinnering.strftime("%Y-%m-%d")}.'
            ))
            return

        self.stdout.write(self.style.NOTICE(
            f"{offertes_voor_herinnering.count()} offerte(s) gevonden voor herinneringen."
        ))

        geadresseerden_geteld = 0
        succesvol_verzonden = 0

        for offerte in offertes_voor_herinnering:
            geadresseerden_geteld += 1
            subject = f"Herinnering: Uw Retrosnacks evenement op {offerte.gewenste_datum.strftime('%d-%m-%Y')}"

            # Stel het platte tekst bericht samen
            plain_message = f"""
Beste {offerte.naam_contactpersoon},

Gelieve niet op deze mail te antwoorden, dit is een automatische verzending.

Dit is een vriendelijke herinnering dat uw evenement met Retrosnacks gepland staat voor:
Datum: {offerte.gewenste_datum.strftime('%d-%m-%Y')}
Tijd: {offerte.gewenste_tijd.strftime('%H:%M')}

Details van uw boeking:
- Formule: {offerte.formule}
- Aantal personen: {offerte.aantal_personen}
- Locatie: {offerte.event_adres if offerte.event_adres else f'{offerte.straat} {offerte.nummer}, {offerte.gemeente}'}

Indien u vragen heeft of wijzigingen wilt doorgeven, neem dan gerust contact met ons op via info@retrosnacks.be.

Met vriendelijke groeten,
Kobe van retrosnacks
E: info@retrosnacks.be
"""
            # Probeer de e-mail te versturen
            try:
                send_mail(
                    subject,
                    plain_message,
                    settings.EMAIL_HOST_USER,  # Afzender e-mailadres uit .env/settings.py
                    [offerte.email],          # Lijst met ontvanger(s)
                    fail_silently=False,      # True om geen error te geven bij falen, False is beter voor debugging
                )
                self.stdout.write(self.style.SUCCESS(
                    f"Herinnering succesvol verzonden naar {offerte.email} voor offerte ID {offerte.id}"
                ))

                # Markeer dat de herinnering is verstuurd om dubbele mails te voorkomen
                offerte.herinnering_verstuurd_op = timezone.now()
                offerte.save(update_fields=['herinnering_verstuurd_op'])
                succesvol_verzonden +=1

            except Exception as e:
                self.stderr.write(self.style.ERROR(
                    f"Fout bij het verzenden van e-mail naar {offerte.email} voor offerte ID {offerte.id}: {e}"
                ))

        self.stdout.write(self.style.SUCCESS(
            f"Script voltooid. {succesvol_verzonden} van de {geadresseerden_geteld} herinnering(en) succesvol verwerkt en verzonden."
        ))