# The Digital Ilse Aichinger List of Literature (`dial`)

The _Digital Ilse Aichinger List of Literature_ (`dial`) aims at bibliographically listing as many published texts as possible by Ilse Aichinger (1921–2016). A complete bibliography has not yet been provided. Holdings of various archives and catalogs were searched, above all from the _Deutsches Literaturarchiv Marbach_ (`DLA`), who also funded the project within the framework of the _Forschungsverbund MWW_ with a fellowship. The `dial` thus comprises 1932 entries at the moment, 665 of which are to be understood as original publications and thus as work entities (as of February 2020).

## Prerequisites and how to use

The file `dial_[#date].bib` is a text file which follows the syntax of `BibLatex` (see [ctan.org/pkg/BibLatex](https://ctan.org/pkg/BibLatex)). It can either be set with `Latex` for example into a `PDF` (see [Comprehensive TeX Archive Network](https://ctan.org/)) or imported into software which can process the format (for example [JabRef](https://www.jabref.org/)).

In the long-term archive of the _Austrian Academy of Sciences_ [ARCHE](https://arche.acdh.oeaw.ac.at/) the current state of the `dial` is stored (Repository ID: _dial_12450_). In addition, it was imported to [Wikidata](https://www.wikidata.org) ([Q54007056](https://www.wikidata.org/wiki/Q54007056)) with the corresponding vocabulary, so that the bibliogaphical data are openly accessible and changeable.

## Research sources

The basis of the `dial` are the holdings of archives and their (mostly digital) catalogues. Especially helpful were the media documentation of the _DLA Marbach_ (DLA Marbach / Z:Aichinger, Ilse, 24 folders) and the catalogue of the _Literaturhaus Wien_. All in all, research was conducted in the holdings of the following institutions:

* _Deutsche Literaturarchiv Marbach_, where the _Nachlass_ of Ilse Aichinger and her husband Günter Eich is archived,
* and with the _S. Fischer Verlagsarchiv_,
* and a rich _Mediendokumentation_,
* the _Kontobücher_ from the literature agentcy _Ruhr-Story_
* and the _Kallías_ catalogue;

* the rich catalogue of the _Literaturhaus Wien_;

* the _Innsbrucker Zeitungsarchiv_;

* the „kommentiertes [Verzeichnis der Literaturzeitschriften in Österreich 1945–1990](www.onb.ac.at/oe-literaturzeitschriften/) of the _Österreichischen Nationalbibliothek_;

* the _Otl Aicher Archiv_ of the _Hochschule für Gestaltung_ in Ulm,

* different bibliographies and bibliographies of bibliographies;

* the _Österreichische Verbundkatalog_;
* the catalogue of the _Deutschen Nationalbibliothek_;
* the Zeitschriftendatenbank _ZDB_;
* the _KVK – Karlsruher Virtueller Katalog_;

* and the library of the _Arbeiterkammer_ in Vienna.

Apart of this, following digital corpora have been checked:

* the _AAC-Austrian Academy Corpus_ of the _Österreichischen Akademie der Wissenschaften_,
* _ANNO - AustriaN Newspapers Online_ of the _Österreichischen Nationalbibliothek_,
* the _WISO Datenbank_,
* the website of the austrian newspaper _Der Standard_,
* the digital _Neue Rundschau Archiv_ and
* the digitalised archive of the programs of the Volkshochschul of the _Deutschen Instituts für Erwachsenenbildung_ [die-bonn.de](www.die-bonn.de).

## Specific Explanations

A declared goal of the project was to work in a pragmatic way with the basic idea of the `FRBR` model. The `FRBR` model distinguishes between _work_, _expression_, _manifestation_ and _example_; which is too differentiated for the purposes of this project, but whose basic idea seemed useful: the possibility to connect texts that are probably to be regarded as 'same' to each other in a specific way. Finally the platform _Wikidata_ was used, because it offers an open and extensible infrastructure.

### Work entities & Wikidata

The field `wikidata` is not part of the `BibLatex` syntax. In _Wikidata_ the project `dial` has the identification number [Q54007056](https://www.wikidata.org/wiki/Q54007056). In it all work units of the `dial` are collected: each with its own _Wikidata_ ID. If a work has been published more then once, the same _Wikidata_-ID is given to each of these publication in the `BibLatex` file. Thus the different publications are connected with each other.

### First publications and genre

In order to make the first publications in particular easy to query, only the units regarded as first editions were provided with a term for the genre (in the `keywords` field). The following genres were used:

* prose
* verse
* drama
* prosepoetry
* interview

### PDF

The attached PDF export was created on 31.1.2020 per `Latexmk` (version 4.41), that is `pdfTeX` (version 3.14159265-2.6-1.40.18, `TeX Live` 2017/Debian). The consecutive numbering is only stable with this specific bib-file and should not be used as a reference.

### HTML

The `bib` file can also be searched locally in the browser with a `JavaScript`-script from _pcooksey_ [bibtex-js](https://github.com/pcooksey/bibtex-js). The most up to date version, although not stable, can be searched at <dial.aichingerhaus.at> per [ItemsJS](https://github.com/itemsapi/itemsjs/).

## further reading

More detailed information can be found in my article „dial. Das Ilse Aichinger Literaturverzeichnis. Methoden, Quellen und eine erste Auswertung des Literaturverzeichnisses“ (in: _[digital humanities austria 2018](doi.org/10.1553/dha-proceedings2018)_, pp. 34–39) zu finden.


## Signe

Andreas Dittrich, Wuppertal, 31.1.2020

## License

This project is licensed under CC-BY 4.0.

## Acknowledgments

The `dial` was made possible by the _Digital Humanities_ scholarship of the [Forschungsverbund MWW](http://www.mww-forschung.de/), to which I am indebted. In addition I would like to thank the employees of the DLA (especially Laura Marie Pohlmann, Karin Schmidgall and Janet Dilger), furthermore to:

* Hanno Biber of the `ICLTT/AC` at the _Austrian Academy of Sciences_,
* Martina Trognitz of the `ACDH` at the _Austrian Academy of Sciences_,
* Martin Mäntele of the _Hochschule für Gestaltung_ (Ulm) and
* the employees of the _Innsbrucker Zeitungsarchiv_ (IZA).

Above all, I would like to thank Christine Ivanovic (_University of Vienna_) for her support, without whom the project could not have started in the first place: thank you very much!