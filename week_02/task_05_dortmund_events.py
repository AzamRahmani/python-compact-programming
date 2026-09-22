from datetime import date

events = {
    "Dublettenflohmarkt": date(2026, 9, 19),
    "Eine Seite Zeitung für Zuhause": date(2026, 9, 19),
    "Keycabs - Kunst unter den Fingerspitzen": date(2026, 9, 19),
    "Kinderspiele wie im Mittelalter": date(2026, 9, 19),
    "Feurige Mitmachstationen": date(2026, 9, 19),
    "Mittelalterliche Mitmach-Musik": date(2026, 9, 19),
    "Bogenschießen für Kinder": date(2026, 9, 19),
    "Die Kuh Lieselotte - Autorenlesung": date(2026, 9, 19),
}

museum_night_date = date(2026, 9, 19)

print("Events during the Dortmund Museum Night:")
print()

for event_name, event_date in events.items():
    if event_date == museum_night_date:
        print(f"- {event_name}: {event_date.strftime('%d.%m.%Y')}")