# TAL

## 1 - Evaluation de l’analyse morpho-syntaxique de la plateforme NLTK 

### 1) 

`python3 MorphoSyntaxique.py`

### 2)

évalution : 93.6%
`python3 evaluate.py wsj_0010_sample.txt.pos.nltk wsj_0010_sample.pos.ref`

### 3) 

`python3 toUniv.py`

évaluation : 97.7%
`python3 evaluate.py wsj_0010_sample.txt.pos.univ.nltk wsj_0010_sample.txt.pos.univ.ref`

A partir des deux évaluations précédentes, nous pouvons observer que nous obtenons de meilleurs résultats grâce aux étiquettes universelles. Celles-ci sont moins spécifiques et correspondent donc à plusieurs étiquettes du Penn TreeBank.

## 2 - Utilisation de la plateforme NLTK pour l’analyse syntaxique

### 1) 

`python3 chunking.py "det-adj-nom"`

### 2) 

Le fichier *chunks.py* regroupe les structures syntaxiques implémentées.

Exemple de test :
`python3 chunking.py "adj-nom"`

## 3 - Utilisation de la plateforme NLTK pour l’extraction d’entités nommées

### 1)

`python3 entiteNommee1.py wsj_0010_sample.txt`

### 2)

`python3 entiteNommee2.py formal-tst.NE.key.04oct95_sample.txt`

### 3)

`python3 entiteNommee1.py formal-tst.NE.key.04oct95_sample.txt`

`python3 entiteNommee2.py formal-tst.NE.key.04oct95_sample.txt`