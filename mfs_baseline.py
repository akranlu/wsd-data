import argparse
from nltk.corpus import wordnet as wn
from collections import defaultdict
import json

datasets = ['ALL', 'sem']

def wn_first(lemma, pos = None):
    for l in wn.synsets(lemma, pos)[0].lemmas():
        key = l.key()
        if key.startswith('{}%'.format(lemma)):
            res = key
            break
        else:
            res = ''
    return res

pos = {
    'VERB': 'v',
    'NOUN': 'n',
    'ADJ': 'a',
    'ADV': 'r'
}

with open(f'data/outputs/{args.dataset}_mfs.txt', 'w') as fw:
    with open('data/jsonl/{args.dataset}.jsonl', 'r') as f:
        for line in f:
            items = json.loads(line)
            mfs = wn_first(items['lemma'], pos[items['pos']])
            out = f'{items["id"]} {mfs}\n'
            fw.write(out)