#!/usr/bin/env python3
import re
import roman

with open("../dial2.bib", "r") as fh:
	bib = fh.read()

# Typographische Anpassungen:
bib = re.sub("\\\\enquote{(.+?)}",r"»\1«",bib) # Latex-Quotation austauschen
bib = re.sub("\\\\emph{(.+?)}",r"\1",bib) # Latex-Quotation austauschen
bib = re.sub("„","»",bib) # Anführungszeichen austauschen
bib = re.sub("“","«",bib) # Abführungszeichen austauschen
bib = re.sub("--","–",bib) # Bindestriche austauschen
bib = re.sub("~"," ",bib) # Gesicherte Spaces austauschen
bib = re.sub("\\\\&","&",bib) # Und-Zeichen austauschen
bib = re.sub("%.+?@","@",bib, flags=re.MULTILINE|re.DOTALL) # %-Umgebung aus dial entfernen

# Seitenanzahl-Skript
def rechner(von, bibtexparser):
	seitenanzahl = int(bis) - int(von) + 1
	if seitenanzahl == 2:
		entry['seiten'] = '2 Seiten'
	elif seitenanzahl == 3:
		entry['seiten'] = '3 Seiten'
	elif seitenanzahl == 4:
		entry['seiten'] = '4 Seiten'
	elif 5 >= seitenanzahl <= 10:
		entry['seiten'] = '5–10 Seiten'
	elif seitenanzahl > 10:
		entry['seiten'] = 'mehr als 10 Seiten'

# BIBTEX parsen und nach JS exportieren:
import bibtexparser
from bibtexparser.bparser import BibTexParser
parser = BibTexParser()
parser.ignore_nonstandard_types = False
bibdb = bibtexparser.loads(bib, parser)

with open("dial2.js", "w") as fh:
	fh.write('var rows = [\n')
	for entry in bibdb.entries:
		fh.write(' {\n')

		if 'crossref' in entry:
			try:
				for entry2 in bibdb.entries:
					if entry['crossref'] == entry2['ID']:
						entry['booktitle'] 	= entry2['title']
						# entry['editor'] 	= entry2['editor']
						# entry['date'] 		= entry2['date']
						# entry['publisher'] 	= entry2['publisher']
						# entry['location'] 	= entry2['location']
					else:
						continue
			except:
				print('Crossref-Fehler bei "', entry['ID'], '" zu "', entry['crossref'], '"')
				continue


		# Datum > Jahr & Jahrzehnt:
		if 'date' in entry:
			if re.findall('^\d+', entry['date']):
				entry['Jahr'] = entry['date'][:4]
				entry['Jahrzehnt'] = entry['date'][:3]+'0er'
			else:
				entry['Jahrzehnt'] = '[o.A.]'
			if len(entry['date']) > 10:
				entry['date'] = re.sub('/',' / ',entry['date'])
		else:
			entry['Jahr'] = 'ohne Jahr'

		# Datum > Datumsangabe:
		if 'date' in entry:
			# Wenn Monat, Jahr
			try:
				dat = re.findall('(\d{4})-(\d{2})$', entry['date'])
				mon = ['','Jänner','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember']
				entry['datum'] = 'im '+mon[int(dat[0][1])]+' '+str(int(dat[0][0]))
			except:
				pass
			# Wenn Tag, Monat, Jahr
			try:
				dat = re.findall('(\d{4})-(\d{2})-(\d{2})', entry['date'])
				entry['datum'] = 'am '+str(int(dat[0][2]))+'.'+str(int(dat[0][1]))+'.'+dat[0][0]
			except:
				pass

		# Publikationsform:
		if 'ENTRYTYPE' in entry:
			if entry['ENTRYTYPE'] ==     'article':
				entry['ENTRYTYPE'] =     '📰 Artikel'
			elif entry['ENTRYTYPE'] == 'mvbook':
				entry['ENTRYTYPE'] =   'mehrbändiges Buch'
			elif entry['ENTRYTYPE'] ==   'book':
				entry['ENTRYTYPE'] =     '📕 Buch '
			elif entry['ENTRYTYPE'] == 'collection':
				entry['ENTRYTYPE'] =   '📙 Sammelband'
			elif entry['ENTRYTYPE'] == 'inbook' or entry['ENTRYTYPE'] == 'incollection':
				entry['ENTRYTYPE'] =   '📖 Buchbeitrag'
			elif entry['ENTRYTYPE'] == 'suppbook':
				entry['ENTRYTYPE'] =   '🔖 Paratext'
			elif entry['ENTRYTYPE'] == 'thesis':
				entry['ENTRYTYPE'] =   '📗 Diss.'
			elif entry['ENTRYTYPE'] ==   'misc':
				if 'howpublished' in entry:
					entry['ENTRYTYPE'] = entry['howpublished']
				else:
					print('Error: no "howpublished" field.')
			else:
				entry['ENTRYTYPE'] = 'sonstiges'
		else:
			print('Error: No "ENTRYTYPE"!')
		
		if 'volume' in entry:
			entry['volume'] = re.sub(' Jahrgang','Jg.',entry['volume'])
	
		if 'keywords' in entry:
			entry['keywords'] = re.split(',',entry['keywords'])
			#entry['volume'] = re.sub(' Jahrgang','Jg.',entry['volume'])

		# Seitenanzahl:
		if 'pages' in entry:
			# Wenn lat. Zahlenraum (wie '2–5'):
			if re.findall('\d+–\d+', entry['pages']):
				entry['pages'] = 'S. ' + entry['pages']
				num = re.findall('(\d+)–(\d+)', entry['pages'])
				von = num[0][0]
				bis = num[0][1]
				rechner(von, bis)
			# Wenn lat. Zahl (wie '2'):
			elif re.findall('\d+[^–]?', entry['pages']):
				entry['pages'] = 'S. ' + entry['pages']
				entry['seiten'] = '1 Seite'
			# Wenn röm. Zahlenraum (wie 'vi–vii'):
			elif re.findall('[a-z]+–[a-z]', entry['pages'], flags=re.IGNORECASE):
				num = re.findall('([a-z]+)–([a-z]+)', entry['pages'])
				von = roman.fromRoman(num[0][0].upper())
				bis = roman.fromRoman(num[0][1].upper())
				rechner(von, bis)
			# Wenn röm. Zahlen (wie 'vii'):
			elif re.findall('^[a-z]+[^–]?', entry['pages'], flags=re.IGNORECASE):
				entry['pages'] = 'S. ' + entry['pages']
				entry['seiten'] = '1 Seite'
			# Wenn Buchstabenkombi (wie 'A12'):
			elif re.findall('^[a-z]\d+', entry['pages'], flags=re.IGNORECASE):
				entry['pages'] = 'S. ' + entry['pages']
			# sonstiges (wie '[nicht autopsiert]')
			else:
				entry['pages'] = entry['pages']
				entry['seiten'] = 'o.A.'
		
		# Wenn Sprache
		if 'language' in entry:
			if entry['language'] == 'british':
				entry['language'] = 'Englisch'
			if entry['language'] == 'american':
				entry['language'] = 'Englisch'
			if entry['language'] == 'German':
				entry['language'] = 'Deutsch'
			if entry['language'] == 'french':
				entry['language'] = 'Französisch'
			if entry['language'] == 'italian':
				entry['language'] = 'Italienisch'
			if entry['language'] == 'japanese':
				entry['language'] = 'Japanisch'
		else:
			entry['language'] = 'Deutsch'

		# Wenn URL == ja
		if 'url' in entry:
			entry['urlb'] = 'ja'
		else:
			entry['urlb'] = 'nein'
		# multiple Autoren:
		if 'author' in entry:
			entry['author'] = re.sub('[\{\}]', '', entry['author'])
			entry['author'] = re.sub(' AND ', ' & ', entry['author'])
		# multiple Buch-Autoren:
		if 'bookauthor' in entry:
			entry['bookauthor'] = re.split(' AND ', entry['bookauthor'])
		# multiple Orte:
		if 'location' in entry:
			entry['location'] = re.split(' AND ', entry['location'])
		# multiple Verlage:
		if 'publisher' in entry:
			entry['publisher'] = re.split(' AND ', entry['publisher'])
		# multiple Herausgeber:
		if 'editor' in entry:
			entry['editor'] = re.sub('[\{\}]', '', entry['editor'])
			entry['editor'] = re.sub(' AND ', ' & ', entry['editor'])
		# Schreiben:
		for element in entry:
			if isinstance(entry[element], str):
				fh.write(
					'  "'+element+'": "'+entry[element]+'",\n')
			elif isinstance(entry[element], list):
				fh.write('  "'+element+'": '+str(entry[element])+',\n')
			else:
				print('Error:', entry[element])
		fh.write(' },\n')
	fh.write(']')

# aktuelles Datum einfügen
from datetime import date
d1 = date.today().strftime('%Y-%m-%d') # computerlesbar
d2 = date.today().strftime('%-d.%-m.%Y') # menschenlesbar
with open("index.html", "r") as fh:
	tmp = fh.read()
	tmp = re.sub(
		'meta name="date" content="\d{4}-\d{2}-\d{2}"',
		'meta name="date" content="'+d1+'"',
		tmp)
	tmp = re.sub(
		'Stand: \d{1,2}\.\d{1,2}\.\d{4}',
		'Stand: '+d2,
		tmp)
with open("index.html", "w") as fh:
	fh.write(tmp)
