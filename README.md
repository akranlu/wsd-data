# wsd-data
Standardized datasets (in `jsonl`) for Word Sense Disambiguation (SemCor and data sets from [Raganato et al., 2017](https://aclanthology.org/E17-1010/), for now.)

## Reproducing

Clone the repository using:
```bash
git clone git@github.com:akranlu/wsd-json.git
```

Create the `data/` directory:
```bash
cd wsd-json
mkdir data
```

Download the Unified WSD evaluation files from [here](http://lcl.uniroma1.it/wsdeval/), unzip it, and store the following directories into the `data/` directory:
```bash
ALL # found in WSD_Evaluation_Framework/Evaluation_Datasets/
semeval2007 # found in WSD_Evaluation_Framework/Evaluation_Datasets/
semeval2013 # found in WSD_Evaluation_Framework/Evaluation_Datasets/
semeval2015 # found in WSD_Evaluation_Framework/Evaluation_Datasets/
senseval2 # found in WSD_Evaluation_Framework/Evaluation_Datasets/
senseval3 # found in WSD_Evaluation_Framework/Evaluation_Datasets/
SemCor # found in WSD_Evaluation_Framework/Training_Corpora/
```

Then, run the following command to convert the xml and txt files in each of the above datasets into jsonl files, stored in `data/jsonl/`:
```bash
python convert.py
```

This script converts the datasets into jsonl files with the following format for each entry:

```json
{
    "id": "id as mentioned in wsd datasets.",
    "word": "<the word>",
    "start": "<start index of the span>",
    "end": "<end index of the span>",
    "sense": "<WordNet sense key>",
    "lemma": "<Lemma of the word>",
    "pos": "<Part of speech tag of the word in the context>",
    "sentence": "<sentence containing the sense-annotated word>"
}
```

## Citation

This script only converts the original data provided by Raganato et al., 2017. Please cite the original authors using this bibtex:
```latex
@inproceedings{raganato-etal-2017-word,
    title = "Word Sense Disambiguation: A Unified Evaluation Framework and Empirical Comparison",
    author = "Raganato, Alessandro  and
      Camacho-Collados, Jose  and
      Navigli, Roberto",
    booktitle = "Proceedings of the 15th Conference of the {E}uropean Chapter of the Association for Computational Linguistics: Volume 1, Long Papers",
    month = apr,
    year = "2017",
    address = "Valencia, Spain",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/E17-1010",
    pages = "99--110",
    abstract = "Word Sense Disambiguation is a long-standing task in Natural Language Processing, lying at the core of human language understanding. However, the evaluation of automatic systems has been problematic, mainly due to the lack of a reliable evaluation framework. In this paper we develop a unified evaluation framework and analyze the performance of various Word Sense Disambiguation systems in a fair setup. The results show that supervised systems clearly outperform knowledge-based models. Among the supervised systems, a linear classifier trained on conventional local features still proves to be a hard baseline to beat. Nonetheless, recent approaches exploiting neural networks on unlabeled corpora achieve promising results, surpassing this hard baseline in most test sets.",
}

```
