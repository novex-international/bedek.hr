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
- **CMS:** Visuelles **Git-basiertes CMS** (Keystatic, alt. Decap) — Kunde editiert grafisch direkt auf der Seite; KI/wir editieren denselben Inhalt parallel per Git/Dateien. Kostenlos, kein Vendor-Lock-in, Inhalte als versionierte MD/JSON. Deckt beide Wünsche ab: Kunde selbst **oder** KI-gesteuert.
- **Styling:** Tailwind CSS mit Custom-Design-Tokens (Luxus × Human)
- **i18n:** Astro i18n-Routing — `/de` (Default/Pitch), `/en`, `/hr`, `/it`. Content je Sprache in strukturierten Daten (JSON/MD) statt hartcodiert.
- **Interaktivität:** minimale JS-Inseln (Multistep-Formular, Sprachwechsler, Mobile-Nav, Chatbot-Widget, Scroll-Animationen)
- **Bilder:** Astro Image-Optimierung (WebP/AVIF, responsive), KI-generierte Assets
- **Deploy:** Netlify (Git-basiert, automatische Builds)
- **Analytics:** Platzhalter für Plausible/GA (datenschutzkonform)

### Komponenten-Isolation (jede Einheit ein Zweck)
- `LanguageSwitcher` — Sprachwahl **mit Landesflaggen** (🇩🇪 Deutsch · 🇬🇧 English · 🇭🇷 Hrvatski · 🇮🇹 Italiano), erhält aktuellen Pfad/Seite beim Wechsel, im Header + Mobile-Nav
- `SiteHeader` / `MobileNav` — Sticky Multi-Channel-Header (Tel, WhatsApp, Sprachen, CTA)
- `Hero` — sektionsweise wiederverwendbar
- `ProblemCards` — problem-geführte Navigation ("Mir fehlt ein Zahn")
- `CostComparison` — Tabelle DE↔HR mit Ersparnis; **optional als interaktive Demo/Rechner** (Besucher wählt Behandlung → sieht Preis HR vs. DE + Ersparnis %). Klein, isoliert, nur wenn gewünscht.
- `MapSection` — Google-Maps-Einbettung + "Route planen"-Button (öffnet Maps-Navigation) + Parkhinweis
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
   - **Google-Reviews-Highlight (authentische Kacheln):** Reviews als **echte Google-Style-Kacheln** wie auf Weltklasse-Seiten — pro Kachel: Avatar/Initiale, Name, ★★★★★, relatives Datum, Review-Text, **Google-„G"-Logo**, dazu Gesamt-Badge „5,0 ★ · Google". **Phase 2:** Live via **Google Places API** (Place-ID gesichert) → Kacheln aktualisieren sich automatisch. Demo: echte Quotes in identischer Kachel-Optik. Link aufs Google-Profil.
   - CTA-Sektion (Formular/Buchung)
2. **Leistungen (`/de/leistungen`)** — Implantate, Kronen/Veneers, Bleaching, allg. Zahnmedizin; je Behandlung Nutzen, Ablauf, Material/Marken, Preisrahmen
3. **Dentaltourismus (`/de/zahntourismus`)** ⭐ Kern-Funnel:
   - Warum Kroatien / Zagreb (Qualität, gleiche Premium-Marken, Ersparnis)
   - **Kostenvergleich-Tabelle** DE↔HR (50–80 % Ersparnis)
   - **Krankenkassen-Erstattung** (EU-RL 2011/24, §13 SGB V): 4-Schritt HKP-Ablauf, was genehmigungspflichtig ist, ehrliche Hinweise (Eigenanteil, Reise, Gewährleistung)
   - **Diaspora-Block** (HR/DE): Heimat + Behandlung kombinieren
   - Anreise nach Zagreb / Ablauf einer Reise
   - FAQ
4. **Über uns / Team (`/de/team`)** — 3-Generationen-Familiengeschichte als Kern-Narrativ + Behandler-Profile + Philosophie + Ausstattung der renovierten Praxis. Team:
   - **dr.sc. Ivan Bedek, dr.med.dent.** (geb. 1979) — Inhaber, Studium Zagreb 2004, Promotion 2019 (Diss.: Zahnalter-Bestimmung bei Kindern via digitalem OPG), Übernahme der Praxis 2014. *(Logo führt "mr.sc.", korrekt seit 2019: dr.sc.)*
   - **Martina Laktić, dr.med.dent.** (geb. 1993) — Studium Zagreb 2018, Dekans- & Rektor-Preis; Schwerpunkte Familienzahnmedizin & Endodontie. *(Genaue aktuelle Titel mit ihr bestätigen — Kunde nennt "MD, PhD".)*
   - **Aktives Behandler-Team:** Ivan Bedek + Martina Laktić.
   - **Marija Bedek, dr.med.dent.** (geb. 1952) — Gründerin/Legacy, **nicht mehr aktiv in der Praxis**. Erscheint nur als Teil der Gründungs-/Familiengeschichte, nicht als aktive Behandlerin.
   - **Narrativ:** "Familientradition, über 30 Jahre Vertrauen" — Gründung durch Marija 1991 → Übernahme & Weiterführung durch Ivan 2014 (promoviert) → heutige Praxis mit Ivan & Martina. Verbindet "old school"-Qualität + Wissenschaft + familiäre Wärme = Luxus × Human.

   **Vollständige Vita (von bedek.hr übernommen, redaktionell optimiert, ohne inhaltliche Verfälschung):**
   - **Ivan Bedek:** geb. 22.08.1979 Zagreb. Klassisches Gymnasium (Abitur 1998), Studium Zahnmedizin Universität Zagreb (Stipendiat), Diplom 26.05.2004 (Thesis: zahnärztliche Behandlung von Kindern mit besonderen Bedürfnissen). Magister 02/2010 (Erosionspotenzial häufig konsumierter Getränke in der Adoleszenz). 2014 eigene Praxis (nach Jahren bei Dr. Marija Bedek & Oralchirurg Dr. Tihomir Švajhler). **Promotion 12.12.2019** (Dissertation: kroatischer Standard zur Bestimmung des Zahnalters von Kindern anhand digitaler OPGs). Regelmäßige fachliche & wissenschaftliche Weiterbildung im In- und Ausland. Verheiratet, zwei Kinder.
   - **Martina Laktić:** geb. 1993 Zagreb. Studium Zahnmedizin Universität Zagreb, Diplom 2018 (Thesis: Zahnerosion). Auszeichnungen: **Dekans-Preis**, **Rektor-Preis für individuelle wissenschaftliche/künstlerische Arbeit**, **Sonder-Rektor-Preis**. Bereits als Studentin in der Praxis Bedek; breite klinische Erfahrung über alle Bereiche. Schwerpunkte: **Familienzahnmedizin & Endodontie**.
   - **⚠️ Titel-Faktencheck (Pflicht, abzustimmen):** Die englische bedek.hr-Seite labelt beide als "MD, PhD". Faktenlage: Ivan = **dr.sc.** (Promotion 2019) + **dr.med.dent.** → korrekt. "MD" trifft nicht zu (Zahnarzt, kein Humanmediziner). Bei **Martina** nennt die Vita **keinen Doktortitel** → "PhD" ist vermutlich Übersetzungsartefakt; bis zur Bestätigung führen wir sie als **Dr. med. dent. Martina Laktić** (mit ihren Preisen als Exzellenz-Signal), um keine falsche Credential-Behauptung zu machen. **Vor Live mit Dr. Bedek/Martina verifizieren.**
5. **Galerie (`/de/galerie`)** — modernisierte Praxisbilder + Cases
6. **Kontakt (`/de/kontakt`)** — Multistep-Formular, **Google-Maps-Einbettung mit Direkt-Navigation** ("Route planen" öffnet Google/Apple Maps zur Praxis), **Parkhinweis** ("In 1 Min. Laufnähe findet sich immer ein Parkplatz"), WhatsApp/Telefon, Buchung, Öffnungszeiten. Adresse Zatišje 6/1 (im hinteren Hof) klar beschrieben, damit Auswärtige sie finden.

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

#### Rechtliche Validierung & Disclaimer (Pflicht)
Alle Aussagen werden gegen **offizielle/autoritative Quellen** geprüft und nur belegt veröffentlicht:
- **EU-Richtlinie 2011/24/EU** (Patientenmobilität) — Bundesgesundheitsministerium (BMG)
- **§13 Abs. 4 & 5 SGB V** — gesetzliche Grundlage der Kostenerstattung im EU-Ausland
- **Bundeszahnärztekammer (BZÄK)** & **KZBV** — Genehmigungspflicht & HKP-Verfahren bei Zahnersatz
- **AOK / Verbraucherzentrale / EVZ** — Festzuschuss, Ablauf, Risiken
- **Nationale Kontaktstelle** eu-patienten.de — offizielle Beratungsstelle

**Regeln für die Texte:**
1. Keine Garantie-Versprechen über Erstattungshöhen — immer "in der Regel ~60 % Festzuschuss der Regelversorgung; exakter Betrag je Kasse & Befund individuell".
2. **Genehmigungspflicht vor Behandlung** klar nennen (sonst Verlust des Zuschusses).
3. Implantate: deutlich machen, dass GKV oft nur den Festzuschuss der Regelversorgung zahlt, Eigenanteil bleibt.
4. **Disclaimer-Box** auf der Zahntourismus-Seite: "Keine Rechts-/Steuerberatung. Erstattung vorab mit der eigenen Krankenkasse klären. Stand: Juni 2026, Quellen verlinkt." + Quellen-Links im Footer/auf der Seite.
5. Klar trennen: was Dr. Bedek leistet (HKP auf deutschem Formular ausstellen) vs. was der Patient/seine Kasse tut.

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

## 11. Phase-2-Punkte — Entscheidungen (Kunden-Input eingearbeitet)
- **Texte & Fotos:** Bestehende bedek.hr-Texte übernehmen, redaktionell optimieren, **für LLM-/KI-Lesbarkeit** strukturieren (semantisches HTML, Schema.org/JSON-LD `Dentist`/`MedicalBusiness`, `llms.txt`) und **für Agentic Commerce** vorbereiten (strukturierte Leistungs-/Preisdaten, maschinenlesbare Endpunkte). Echte Fotos später vom Kunden; vorerst KI-modernisierte Bilder.
- **Preisliste:** **Reale Wettbewerbspreise** kroatischer Kliniken recherchieren und als transparente **Platzhalter-Preise** (klar als Richtwerte gekennzeichnet) einbauen, bis Dr. Bedek seine echte Liste liefert.
- **GHL (Phase 2):** Kunde (Manuel) hat **Agency-Lizenz**, stellt Zugänge bereit. Benötigt: Sub-Account/Location-ID, API-Key, Kalender-ID, **Telefonnummer für Voice AI**, WhatsApp-Anbindung. **KI-Chatbot** mit **Branchenwissen (Dentaltourismus/Zahnmedizin) + Guidelines/Guardrails** (Preise, Ablauf, Kasse, Ton; keine medizinischen Diagnosen, keine Garantie-Versprechen).
- **Domain:** **Bestehende Domain bedek.hr** weiterverwenden; Deploy auf **Manuels Netlify-Account**; Demo zunächst Netlify-Subdomain, dann bedek.hr umstellen.
- **Festzuschuss 2026:** Aktuelle Werte recherchieren **und rechtlich verifizieren**; mit Disclaimer + Quellen + "individuell mit Kasse klären".

## 11b. Bild-Pipeline (KI)
- **Arzt-Porträts:** echte Originale (`ivan.png`, `martina.jpg`) im Projekt. Wunsch: KI-**Gleichrichtung** (einheitliche Ausrichtung/Blickrichtung beider Personen) + **Modernisierung/Retusche** — **ohne die Person zu verändern** (Identität erhalten, nur Licht/Schärfe/Hintergrund/Konsistenz).
- **Praxis-Innenräume:** **KI-Bilder auf Basis der alten Raumfotos** erzeugen (gleicher Raum, modernisiert/renoviert) — Bild-zu-Bild, da die Räumlichkeit gleich bleibt.
- **Tooling-Hinweis:** In dieser Umgebung **kein natives Bild-KI-Tool**. Umsetzung über externes Bildmodell (OpenAI `gpt-image-1` Edit, Google Imagen/"nano banana", Flux via fal/Replicate) per Skript (mit `truststore` wegen TLS-Interception) **oder** extern generiert & eingespielt. Entscheidung offen (siehe Frage).
- **Demo-Fallback:** echte Porträts as-is + premium Stock-Interieurs; KI-Bilder werden nachgeschoben, sobald Provider/Key feststeht.

## 12. Design-Exploration
Vor dem Vollausbau: 3 HTML-Mockups der Startseite in distinkten Richtungen (A: Editorial Luxury · B: Warm Human · C: Modern Bold Premium) → Kunde wählt Richtung → Vollausbau mit Sub-Agents.
