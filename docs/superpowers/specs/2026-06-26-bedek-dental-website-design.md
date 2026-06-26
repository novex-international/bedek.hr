# Dr. Bedek Dental — Website & Patientengewinnungssystem

**Datum:** 2026-06-26
**Status:** Design / Spec (zur Freigabe)
**Zweck:** Weltklasse, mehrsprachige Website für die Zahnarztpraxis *mr.sc. Ivan Bedek, dr.med.dent.* (Zagreb) mit Fokus auf internationalen Dentaltourismus (v.a. deutschsprachiger Raum + kroatische Diaspora). Pitch-Demo bis morgen live auf Netlify; danach echte Auslieferung.

---

## 1. Kontext & Ausgangslage

**Praxis:** Ordinacija dentalne medicine mr.sc. Ivan Bedek, dr.med.dent.
**Standort:** Zatišje 6/1, 10000 Zagreb (im hinteren Hof). Tel. +385 95 729 9112.
**Reputation:** Exzellente Reviews ("bester Zahnarzt", "old school", Gesundheit vor Ästhetik, keine unnötigen Eingriffe). Praxis diese Woche frisch renoviert.

**Bestehende Seite (bedek.hr):** Bescheidenes WordPress (WPML + Gravity Forms), dreisprachig HR/EN/IT. Schwächen, die wir adressieren:
- Kein Deutsch (Kernzielgruppe Dentaltourismus fehlt)
- Keine Preise / kein Kostenvergleich
- Keine Dentaltourismus-Story (Ablauf, Anreise, Kassenerstattung)
- Keine sichtbaren Testimonials / Vorher-Nachher
- Generisches Theme, nicht premium

**Referenz-Benchmark (kroatische Wettbewerber):**
- Dentum (7,5/10) — problem-geführte Nav, Dental-Tourism-Seite, VR-Tour, Makeover-Cases, Image-CDN
- Štimac (7,5/10) — symptom-basierte Nav, 5 Sprachen inkl. DE, Trust-Wall
- Identalia (6,5/10) — Länder-getaggte Testimonials, Anreise-/Unterkunft-Seite
- Identa.hr (6,5/10) — Sticky Multi-Channel-Header, 24h-SOS, Partner-Logo-Wall

Keiner erreicht "Luxus × Human Modern" oder kommuniziert die Krankenkassen-Erstattung klar. **Das ist unsere Lücke.**

## 2. Ziele & Erfolgskriterien

1. **Pitch gewinnen:** Dr. Bedek soll beim Termin morgen sofort sehen, dass dies eine Klasse über allem liegt, was er und Wettbewerber haben.
2. **Lead-Conversion:** Internationale Besucher (DE/AT/CH + Diaspora) zu qualifizierten Anfragen konvertieren.
3. **Vertrauen:** Seriöse, ehrliche Kommunikation von Qualität, Preisen und Kassen-Erstattung.
4. **Performance:** Lighthouse ≥ 95 (Performance/SEO/Best Practices/Accessibility), schnelle Ladezeit.
5. **Auslieferbar:** Kein Wegwerf-Prototyp — sauberer Code, der real betrieben werden kann.

## 3. Scope

### In Scope
- Mehrsprachige Multi-Page-Website (DE / EN / HR / IT), **DE als Pitch-Default**
- Dentaltourismus-Funnel mit Krankenkassen-Erstattung, Kostenvergleich, Diaspora-Ansprache
- Custom-designtes Lead-Erfassungssystem (Frontend), vorbereitet für GHL-Backend
- KI-generierte, fotorealistische Bilder + modernisierte Praxisbilder
- Deploy auf Netlify

### Out of Scope (für die Demo; Phase 2)
- Live-Verdrahtung der GHL-Pipeline / Voice AI / Workflows (nach Auftragszusage)
- Echte Patientenfotos/Texte vom Kunden (zunächst KI/Platzhalter, dann ersetzen)
- Blog/CMS-System (später)

## 4. Technische Architektur

- **Framework:** Astro (statische Site, Insel-Architektur, ideal für Netlify + Performance)
- **Styling:** Tailwind CSS mit Custom-Design-Tokens (Luxus × Human)
- **i18n:** Astro i18n-Routing — `/de` (Default/Pitch), `/en`, `/hr`, `/it`. Content je Sprache in strukturierten Daten (JSON/MD) statt hartcodiert.
- **Interaktivität:** minimale JS-Inseln (Multistep-Formular, Sprachwechsler, Mobile-Nav, Chatbot-Widget, Scroll-Animationen)
- **Bilder:** Astro Image-Optimierung (WebP/AVIF, responsive), KI-generierte Assets
- **Deploy:** Netlify (Git-basiert, automatische Builds)
- **Analytics:** Platzhalter für Plausible/GA (datenschutzkonform)

### Komponenten-Isolation (jede Einheit ein Zweck)
- `LanguageSwitcher` — Sprachwahl, erhält aktuellen Pfad
- `SiteHeader` / `MobileNav` — Sticky Multi-Channel-Header (Tel, WhatsApp, Sprachen, CTA)
- `Hero` — sektionsweise wiederverwendbar
- `ProblemCards` — problem-geführte Navigation ("Mir fehlt ein Zahn")
- `CostComparison` — Tabelle DE↔HR mit Ersparnis
- `InsuranceProcess` — 4-Schritt Krankenkassen-Ablauf (HKP)
- `TestimonialCard` — länder-getaggt
- `BeforeAfter` — Vorher/Nachher-Slider
- `LeadForm` (Multistep) — Smile-Assessment + Foto-Upload → GHL-Webhook-Adapter (gestubbt)
- `BookingWidget` — Terminbuchung (Platzhalter für GHL-Kalender)
- `ChatbotWidget` — Floating-Button (Platzhalter für GHL AI-Bot)
- `ContactSection` — Formular, Karte, Kontaktkanäle
- `SiteFooter`

Der **GHL-Adapter** ist eine isolierte Schnittstelle: heute schreibt er in einen Platzhalter/Konsole, später nur Endpunkt/Webhook-URL eintragen — kein Umbau des Frontends nötig.

## 5. Sitemap & Seiten

Jede Seite in 4 Sprachen.

1. **Home (`/de`)**
   - Hero: frisch renovierte Praxis, Kern-Versprechen, primärer CTA
   - Trust-Bar (Erfahrung, Marken Straumann/Nobel, Reviews)
   - Problem-geführte Cards (Implantat, Kronen/Veneers, Bleaching, allg. Zahnmedizin)
   - Dentaltourismus-Teaser (inkl. "Ihre Kasse zahlt mit")
   - Kostenvergleich-Kurzblock
   - Vorher/Nachher
   - Länder-getaggte Testimonials
   - CTA-Sektion (Formular/Buchung)
2. **Leistungen (`/de/leistungen`)** — Implantate, Kronen/Veneers, Bleaching, allg. Zahnmedizin; je Behandlung Nutzen, Ablauf, Material/Marken, Preisrahmen
3. **Dentaltourismus (`/de/zahntourismus`)** ⭐ Kern-Funnel:
   - Warum Kroatien / Zagreb (Qualität, gleiche Premium-Marken, Ersparnis)
   - **Kostenvergleich-Tabelle** DE↔HR (50–80 % Ersparnis)
   - **Krankenkassen-Erstattung** (EU-RL 2011/24, §13 SGB V): 4-Schritt HKP-Ablauf, was genehmigungspflichtig ist, ehrliche Hinweise (Eigenanteil, Reise, Gewährleistung)
   - **Diaspora-Block** (HR/DE): Heimat + Behandlung kombinieren
   - Anreise nach Zagreb / Ablauf einer Reise
   - FAQ
4. **Über uns / Team (`/de/team`)** — Dr. Bedek, "old school" Qualitäts-Story, Philosophie, Ausstattung der renovierten Praxis
5. **Galerie (`/de/galerie`)** — modernisierte Praxisbilder + Cases
6. **Kontakt (`/de/kontakt`)** — Multistep-Formular, Karte, WhatsApp/Telefon, Buchung, Öffnungszeiten

## 6. Inhaltliche Kern-Argumente (recherchiert)

### Kostenvergleich (gleiche Premium-Marken)
| Behandlung | Kroatien | Deutschland | Ersparnis |
|---|---|---|---|
| Einzelimplantat inkl. Krone | €800–1.500 | €1.800–4.000 | 50–70 % |
| Premium-Implantat (Straumann/Nobel) | €750–950 | €1.800–4.000 | 50–80 % |
| Krone (Zirkon/Keramik) | €200–300 | deutlich höher | ~50–70 % |

### Krankenkassen-Erstattung (Vertrauens-Booster)
- Rechtsgrundlage: EU-Richtlinie 2011/24/EU + §13 Abs. 4/5 SGB V; Kroatien seit 2013 EU.
- GKV erstattet **Festzuschuss in Höhe der deutschen Regelversorgung** (~60 %, mit Bonusheft mehr).
- **Zahnersatz/Implantate = vorab genehmigungspflichtig:** Praxis stellt HKP auf deutschem Kassenformular → Patient reicht ihn **vor** Behandlung ein → Kasse prüft (3 Wo.) → genehmigter Zuschuss.
- Genehmigungsfrei: Vorsorge, Füllungen, Wurzelbehandlungen.
- Ehrliche Hinweise: Implantat-Eigenanteil & Reise selbst zahlen; 2 Jahre Gewährleistung; Nachsorge mitdenken.
- USP: Praxis-Service "Wir erstellen Ihren HKP auf deutschem Formular" — fast kein Wettbewerber kommuniziert das.

### Diaspora-Ansprache
- Kroatische Community DE/AT/CH: sprachliche Vertrautheit, Familie, Behandlung + Heimaturlaub.
- Zweigleisiges Messaging: Diaspora (HR/DE emotional) + deutsche Nicht-Diaspora (Ersparnis + Qualität + Städtereise Zagreb).

## 7. Lead-Erfassung & GHL-Strategie

### Weltklasse-Niveau (über das einfache Formular hinaus)
1. Mehrstufiges **Smile-Assessment** mit Foto/Röntgen-Upload (liefert HKP-Infos)
2. **Sofort-Antwort < 60 Sek.** (automatisiert)
3. **WhatsApp-first** Kontakt
4. **Online-Terminbuchung** für kostenloses Video-/Telefon-Erstgespräch
5. **4-sprachiger AI-Chatbot** 24/7
6. **Voice AI + Missed-Call-Textback** — niemand verpasst einen Anruf

### Wow-Fokus (Kundenwunsch)
**Voice AI + Missed-Call-Textback** als Hero-Feature: Telefonassistenz nimmt Terminanfragen an, qualifiziert, und bietet **gezielten Rückruf** oder **Direktbuchung bei planbaren Standard-Eingriffen** (z.B. Zahnreinigung). Löst den Kern-Schmerz: Zahnarzt kann nicht behandeln und gleichzeitig ans Telefon.

### Integrationsweg (Entscheidung: Custom-Frontend, GHL-Wiring danach)
- Custom Astro-Multistep-Formular + Buchung + Chat sichtbar & klickbar.
- Daten gehen vorerst in Platzhalter/Konsole (isolierter GHL-Adapter).
- Nach Auftragszusage: GHL-Pipeline (Anfrage → Foto erhalten → HKP erstellt → Kasse genehmigt → Termin → Behandlung), Voice AI, Workflows, Reputation/Reviews verdrahten.

## 8. Design-System (Luxus × Human Modern)

- **Stimmung:** viel Weißraum, editoriale Typo, warme menschliche Akzente — Premium-Medizin ohne Klinik-Kälte.
- **Farben:** sanftes Teal/Blau (Vertrauen, Medizin) + warmer Sand/Beige-Ton (Wärme, Human) + Off-White-Grund + dunkler Akzent für Kontrast. (Finale Hex-Werte im Plan.)
- **Typografie:** elegante Serif für Headlines (editorial/luxus) + klare Sans für Fließtext.
- **Bilder:** echte Gesichter, frisch renovierte Praxis (KI-modernisiert), Vorher/Nachher.
- **Motion:** dezente Scroll-Reveals, sanfte Hover-States — kein Effekt-Overkill.
- **Vertrauenselemente:** Marken-Logos (Straumann/Nobel), Reviews, Trust-Badges, ehrliche Hinweise.
- **Responsive & Accessible:** Mobile-first, WCAG-AA-Kontraste, Tastatur-Navigation.

## 9. Hosting & Deploy

- **Netlify** (Git-Integration, automatische Builds, kostenloser Tier für Demo).
- Custom-Domain später (z.B. Subdomain oder eigene Domain für Pitch).
- Build: `astro build` → `dist/` → Netlify.

## 10. Phasen

- **Phase 1 (heute, Demo):** Astro-Setup, Design-System, alle 6 Seiten in DE (EN/HR/IT-Gerüst), KI-Bilder, Lead-Formular (gestubbt), Voice-AI-Feature visuell dargestellt, Netlify-Deploy, Lighthouse-Check.
- **Phase 2 (nach Zusage):** Volle 4-Sprachen-Inhalte, echte Bilder/Texte vom Kunden, GHL-Pipeline + Voice AI live, Custom-Domain, Reviews-Automation.

## 11. Offene Punkte (für Phase 2 / Kunden-Input)
- Finale Texte & echte Fotos von Dr. Bedek
- Tatsächliche Preisliste der Praxis
- GHL-Account-Details / Telefonnummer für Voice AI
- Domain-Wahl
- Genaue Festzuschuss-Werte 2026 (Patient klärt individuell mit Kasse — wird so kommuniziert)
