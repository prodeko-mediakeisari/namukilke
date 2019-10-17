# Namukilke :candy: :apple:

Python 3.6.7 | Django 2.1.0

Pyörii palvelimella virtuaaliympäristön sisällä `source venv/bin/activate`. Aja tämä komento sudolla!

Käytetään tabletilla ja kiltiskoneella kiltiksen wlanin yli.

Toistaiseksi tuotekuvien hallintaan ei ole admin käyttöliittymää. Uutta tuotetta luodessa tuotekuva täytyy lisätä palvelimelle kansioon `namu/static/img`, johon Namusetä tarvinnee Webbitiimin apua.

Kuvien lisäämisen jälkeen aja `python3 manage.py collectstatic`. Tarvittaessa käynnistä myös Apache uudestaan.

## Todo-lista

Päivitetty 22.12.2018

- [x] Zoomauksen fiksaaminen deposit-sivulla (auto zoom-out tai disable zoom)
- [ ] Feedback form tuotetoiveita varten etusivulle tai ostamissivulle (Google form tai Django form)
- [x] Tuotelistauksen järjestäminen käyttäjäkohtaisesti suosituimmat tuotteet ensin
- [x] Statistiikkasivu (namu.prodeko.org/stats)
- [ ] Statistiikkasivun jatkokehitys: hävikki, käyttäjä- ja tuotekohtaiset tilastot
- [ ] Admin käyttöliittymä tuotekuvien lisäämiseen palvelimelle
- [ ] Ostaminen AJAX post jotta helpompi ostaa useita tuotteita
- [ ] Timeout uloskirjautuminen esim. 1min epäaktiivisuuden jälkeen
- [ ] Tuotenimien ja varastosaldon rivitys tuotelistauksessa. Esim. max pituus nimelle tai korttien koon kasvattaminen.
- [ ] Ostoilmoituksen modalin koon ja tekstin rivittämisen korjaaminen
