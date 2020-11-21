# NamSor Bio-Cultural Diversity visualization

The onomastic mille-feuille is a simple visualization for tabular data, where different colors reprensent different NamSor classes (ex. gender, US'race'/ethnicity, origin/country/diaspora ... or a combination of those) stacked in ordinate.
In abscissa, any grouping can be chosen : it could be geographic (country or region ...), or other features such as a job type, an interest, a language.

All NamSor artworks are released as Creative Commons CC-BY-4.0
https://creativecommons.org/licenses/by/4.0/

## 'Origin', Elian Carsenat, 07-2020
'Origin' is a back-testing of NamSor Origin API v2.0.10 on Wikidata names (20200513_WW_WikiData.sql and 20200526_WikiData_NamSorV2010_BackTest_vF.xlsx/fnln_origin_confusion).
It reflects how correlation between personal names and a particular country of origin (as recognized by Origin API v2.0.10). The onomastic mille-feuille was post-processed with Inkscape to add a mirror effect. 

![Origin, Elian Carsenat, 07-2020](artwork/072929_Origin/20200807_Millefeuilles_Origin_Wikidata_v2010_post_A0_150DPI.png?raw=true "Origin")

## 'Chinese sea', Elian Carsenat, 08-2020
'Chinese sea' is a colorful view of the cartography of COVID-19 Scientific Literature, from the angle of nationality / country of origin or ethnicity of scientists across 30 different subject clusters.
![Chinese sea, Elian Carsenat, 08-2020](artwork/082020_ChineseSea/20200806_Millefeuilles_A0v001_170DPI.png?raw=true "Chinese sea")

It reflects a collaboration project of Dario Rodighiero (MIT CMS/W / Harvard Metalab), Eveline Wandl-Vogt (Ars Electronica Research Institute knowledge for humanity / Austrian Academy of Sciences), and Elian and Gabriel Carsenat (NamSor).

Using the open-source database COVID-19 Open Research Dataset (CORD-19) released on July 1, 2020 by the Allen Institute for AI, scientific articles are grouped by authors and analyzed with methods of Natural Language Processing.

The canvas shows the pre-eminence of Chinese names across all 30 subject clusters. Their overall share in production of science is the large blue 'sea' making about a third of the canvas.

Apart from China, most countries have worked in silos and focused their effort on one single subject. So their combined production of science looks like a mountainous shore.
Find the source code on Github,
https://github.com/namsor/COVID-19#chinese-sea-artwork

This work was first presented at Ars Electronica 2020.
From it were made 15 original and unique prints on A0 foamboard (1189mm X 841mm) with Certificate of Authenticity.


## Running namsor-diversity-viz
Run
`python api.py`

Then post the tabular data to 
http://127.0.0.1:5000/api
and receive the SVG output.


