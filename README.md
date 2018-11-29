# Project Title

Enriching Knowledge Bases with Temporal Meta-facts

## Getting Started

This repository contains the first version of our work titled "Enriching Knowledge Bases with Temporal Meta-facts". Since this is a work in progress, several improvements will be added later. The algorithm that implements the rules can be found in the inferTempMetafactsipynb file. We use the jupyter notebook to facilitate the reproduction of work.

### Prerequisites

To run the inferTempMetafacts.ipynb, you must:

* create a local base with the YAGO files (download [link] (https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/yago/downloads/) - YAGO files used . In addtion, a database script to load YAGO into a Postgres database is also provided in the download link. In this work, we only use some YAGO (.tsv) themes to recreate a portion of the YAGO database. These files are: 
```
- Taxonomy: yagoSchema, yagoTaxonomy, and yagoTypes.
- CORE: yagoFacts, yagoLiteralFacts, and yagoDateFacts.
- Meta: yagoMetaFacts -- temporal and geospatial meta facts of yagoFacts
```
* update the database.ini file with the information from your database.

To run the search_movies.ipynb, update the APIkeys.json file (the file can be found at lib folder)  with your IMDb key.

### Results
* The metafiles obtained can be found at the outputs folder.
* The file that combines the contents of the actedIn.csv file with the IMDb information can be found at imdb folder.
* Information obtained from our first analysis can be found at outputs / matches folder.


## Acknowledgments

*  [Tirthajyoti Sarkar] (https://towardsdatascience.com/step-by-step-guide-to-build-your-own-mini-imdb-database-fc39af27d21b) - Step guide to search IMDb information.