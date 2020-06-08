# Das Digitale Ilse Aichinger Literaturverzeichnis (`dial`)

Das _Digitale Ilse Aichinger Literaturverzeichnis_ (`dial`) setzt sich zum Ziel, möglichst alle publizierten Texte von Ilse Aichinger (1921–2016) bibliografisch zu verzeichnen. Eine vollständige subjektive Personalbibliografie ist bislang nicht geleistet worden.[^1] Für das `dial` wurden Bestände verschiedener Archive und Kataloge durchsucht (siehe Abschnitt [Recherchequellen](#Recherchequellen)); vor allem aber die Bestände am _Deutschen Literaturarchiv Marbach_, welches das Projekt über den _Forschungsverbund MWW_ auch mit einem Stipendium gefördert hat. Das `dial` umfasst derzeit 1932 Einträge, von denen 665 Einträge als Erstpublikationen bzw. Werkeinheiten zu verstehen sind (Stand: Februar 2020).[^2]

## Voraussetzungen und Verwendungsmöglichkeiten

Die Datei `dial_[#date].bib` ist eine Textdatei, welche der Syntax von `BibLaTex` folgt (siehe dazu [ctan.org/pkg/biblatex](https://ctan.org/pkg/biblatex)). Sie kann entweder mit `LaTex` zum Beispiel in ein `PDF` gesetzt werden (siehe [Comprehensive TeX Archive Network](https://ctan.org/)) oder in Software importiert werden, welche das Format verarbeiten kann (beispielsweise [JabRef](https://www.jabref.org/)).

Im Langzeitarchiv der _Österreichischen Akademie der Wissenschaften_ [ARCHE](https://arche.acdh.oeaw.ac.at/) wird der derzeitige Stand des `dial` gesichert (Repository ID: _dial_12450_). Zusätzlich wird es auf [Wikidata](https://www.wikidata.org) ([Q54007056](https://www.wikidata.org/wiki/Q54007056)) mit dem entsprechenden Vokabular importiert, sodass die bibliografischen Daten dort offen zugänglich und veränderbar sind.

## Recherchequellen

Grundlage des `dial` sind die Bestände von Archiven und deren (großteils digitale) Kataloge. Besonders hilfreich waren die entsprechende Mediendokumentation des _DLA Marbach_ (DLA Marbach / Z:Aichinger, Ilse, 24 Mappen) und der Katalog des _Literaturhaus Wien / Dokumentationsstelle für neuere österreichische Literatur_. Insgesamt wurden in den Beständen folgender Insitutionen recherchiert:

* vor allem das _Deutsche Literaturarchiv Marbach_, wo, neben dem _Nachlass_ von Ilse Aichinger und dem ihres Mannes Günter Eich,
* das _S. Fischer Verlagsarchiv_,
* eine reichhaltige _Mediendokumentation_,
* die _Kontobücher_ der (einige Texte von Aichinger vermittelnden) Literaturagentur _Ruhr-Story_ und
* der fein differenzierte und sehr hilfreiche Katalog _Kallías_ zur Verfügung stehen;

* der reichhaltige Katalog des _Literaturhaus Wien_ (der technisch aber dringend einer Überholung bedarf);

* das _Innsbrucker Zeitungsarchiv_ (sowohl [online](www.uibk.ac.at/iza/) als auch vor Ort);

* das kommentierte [Verzeichnis der Literaturzeitschriften in Österreich 1945–1990](www.onb.ac.at/oe-literaturzeitschriften/) der _Österreichischen Nationalbibliothek_;

* das _Otl Aicher Archiv_ der _Hochschule für Gestaltung_ in Ulm,

* verschiedene allgemeine Bibliografien der Literaturgeschichte und Bibliografien von Bibliografien;

* der _Österreichische Verbundkatalog_;
* der Katalog der _Deutschen Nationalbibliothek_;
* die Zeitschriftendatenbank _ZDB_;
* der _KVK – Karlsruher Virtueller Katalog_;

* und die Bibliothek der _Arbeiterkammer_ in Wien (durch deren schnelle Aushebezeiten österr. Zeitungen ein suchendes Arbeiten erst möglich wird).

Zusätzlich wurden folgende digitale Korpora durchsucht:

* das _AAC-Austrian Academy Corpus_ der _Österreichischen Akademie der Wissenschaften_,
* _ANNO - AustriaN Newspapers Online_ der _Österreichischen Nationalbibliothek_,
* die _WISO Datenbank_,
* die Webpräsenz der österr. Tageszeitung _Der Standard_,
* das digitale _Neue Rundschau Archiv_ und
* das digitalisierte Volkshochschul-Programmarchiv des _Deutschen Instituts für Erwachsenenbildung / Leibniz-Zentrum für Lebenslanges Lernen e.V._ [die-bonn.de](www.die-bonn.de).


## Spezifische Erläuterungen

Ein erklärtes Projektziel war es, auf eine pragmatische Weise mit der grundlegenden Idee des `FRBR`-Modells zu arbeiten. Im `FRBR`-Modell wird zwischen _Werk_, _Expression_, _Manifestation_ und _Exemplar_ unterschieden; was für die Zwecke dieses Projekts zu differenziert ist, dessen grundlegende Idee aber brauchbar erschien: die Möglichkeit, Texte, die vermutlich als 'die gleichen' anzusehen sind, miteinander in eine spezifische Verbindung zu bringen. Schließlich wurde die Plattform _Wikidata_ verwendet, da diese eine offene und erweiterbare Infrastruktur bietet.

### Werkeinheiten & Wikidata

Die Datei mit der Endung `bib` folgt im Wesentlichen der Syntax von `BibLaTex`, erweitert diese aber um das Feld `wikidata`, welches von den entsprechenden Parsern ignoriert werden kann. Unter der _Wikidata_-ID [Q54007056](https://www.wikidata.org/wiki/Q54007056) werden alle Werkeinheiten des `dial` gesammelt: jeweils mit einer eigenen _Wikidata_-ID. Wurde ein Werk öfter publiziert, so wird in der BibLaTex-Datei jeder Publikation dieselbe Werk-ID gegeben. Dadurch werden die verschiedenen Publikationen in der `bib`-Datei miteinander verbunden.

### Erstpublikationen und Gattung

Um speziell die Erstpublikationen leicht abfragbar zu machen, wurden nur die jeweils als Erstausgabe angesehenen Einheiten (im Feld `keywords`) mit einem Gattungsbegriff versehen. Folgende Gattungsbezeichnungen wurden dabei verwendet:

* _prose_ für Prosatexte,
* _verse_ für Gedichte,
* _drama_ für szenische Texte mit verteilten Sprechrollen,
* _prosepoetry_ für Prosagedichte und
* _interview_ für abgedruckte Gespräche mit der Autorin.

### PDF

Der beigefügte PDF-Export ist am 31.1.2020 per `Latexmk` (Version 4.41), bzw. `pdfTeX` (Version 3.14159265-2.6-1.40.18, `TeX Live` 2017/Debian) erzeugt worden. Die fortlaufende Nummerierung ist nur mit dieser spezifischen Bib-Datei stabil und sollte nicht als Referenz genommen werden.


### HTML

Die `bib`-Datei kann auch mit einem Javascript von _pcooksey_ [bibtex-js](https://github.com/pcooksey/bibtex-js) im Browser lokal durchsucht werden. Unter der Adresse <dial.aichingerhaus.at> ist eine zwar instabile, aber aktuelle und abfragbare Version des `dial` per [ItemsJS](https://github.com/itemsapi/itemsjs/) möglich.


## weiterführendes und Fußnote

Ausführlichere Informationen sind in meinem Artikel „dial. Das Ilse Aichinger Literaturverzeichnis. Methoden, Quellen und eine erste Auswertung des Literaturverzeichnisses“ (in: _[digital humanities austria 2018](doi.org/10.1553/dha-proceedings2018)_, S. 34–39) zu finden.


[^1]: Siehe die drei bisher ausführlichsten Personalbibliografien von: (1.) Gomboz, Ingrid: „Bibliographie Ilse Aichinger“, in: _Ilse Aichinger_, hrsg. v. Kurt Bartsch und Gerhard Melzer, Droschl: Graz 1993, S. 249–293; (2.) Reichensperger, Richard: „Bibliographie der Werke Ilse Aichingers“, in: _Ilse Aichinger. Leben und Werk. Informationen und Materialien zur Literatur_, akt. und erw. Neuausgabe, hrsg. v. Samuel Moser, 2. Aufl., S. Fischer Verlag: Frankfurt am Main 2003, S. 345–355; (3.) Karnahl, Julia: „Auswahlbibliographie“, in: _Text + Kritik. Zeitschrift für Literatur_ 175 (2007): Ilse Aichinger, hrsg. v. Roland Berbig, S. 112–115.

[^2]: Siehe auch meinen Beitrag: „dial. Das Digitale Ilse Aichinger Literaturverzeichnis. Methoden, Quellen und eine erste Auswertung des Literaturverzeichnisses“, in: _digital humanities austria 2018_, hrsg. v. Marlene Ernst, Peter Hinkelmanns, Lina Maria Zangerl und Katharina Zeppezauer-Wachauer, Austrian Academy of Sciences Press: Wien 2020, [doi:10.1553/dha-proceedings2018s34](doi.org/10.1553/dha-proceedings2018s34).

## Signe

Andreas Dittrich, Wuppertal, am 31.1.2020

## Lizenz

Die Daten dieses Projekts stehen unter der Lizenz CC-BY 4.0.

## Danksagung

Ermöglicht wurde das `dial` durch das _Digital Humanities_ Stipendium des [Forschungsverbund MWW](http://www.mww-forschung.de/), dem ich zum Dank verpflichtet bin. Zusätzlich danke ich den Beschäftigten des _DLA_ (insbesondere Laura Marie Pohlmann, Karin Schmidgall und Janet Dilger) und:

* Hanno Biber des `ICLTT/AC` an der _Österreichischen Akademie der Wissenschaften_,
* Martina Trognitz des `ACDH` der _Österreichischen Akademie der Wissenschaften_,
* Martin Mäntele der _Hochschule für Gestaltung_ (Ulm) und
* den Beschäftigten des _Innsbrucker Zeitungsarchivs_ (IZA).

Vor allem gebührt mein Dank aber der Unterstützung von Christine Ivanovic (_Universität Wien_), ohne der das Projekt erst gar nicht anfangen hätte können: herzlichen Dank!