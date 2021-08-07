import os
import json

import xml.etree.ElementTree as ET

from tqdm import tqdm
from collections import defaultdict
from pathlib import Path

directories = ['SemCor', 'ALL', 'semeval2007', 'semeval2013', 'semeval2015', 'senseval2', 'senseval3']

def parse_sense_data(xml_file, gold_file):
    parsed = ET.parse(xml_file)
    root = parsed.getroot()

    gold = defaultdict(str)

    with open(gold_file, 'r') as f:
        for line in f:
            s = line.split()
            if len(s) > 2:
                synset = ';'.join(s[1:])
                key = s[0]
                gold[key] = synset
            else:
                key, synset = s
                gold[key] = synset

    gold.default_factory = None

    sense_annotations = []
    # sentences = set()
    # pos = defaultdict(int)
    for text in root:
        for j, sentence in enumerate(text):
            s = ' '.join([w.text for w in sentence]).replace('filde', 'filled').replace('do [ c ] ters', 'doctors').replace('``', '"').replace('&apos;&apos;', '"').replace("\''", '"').replace('offersey', 'officers').replace('takeing', 'taking')
            # sentences.add(s)
            current_len = 0
            for i, word in enumerate(sentence):
                text = word.text
                # doing my best to correct some spellings that stand out..
                if text == 'filde':
                    text = 'filled'
                if text == 'do [ c ] ters':
                    text = 'doctors'
                if text == 'offersey':
                    text = 'officers'
                if text == '``':
                    text = '"'
                if text == '&apos;&apos;' or text == "\''":
                    text = '"'
                text = text.replace('takeing', 'taking')
                length = len(text.split(" "))
                current_len += length
                if word.tag == 'instance':
                    # pos[word.attrib['pos']] += 1
                    start = current_len - length
                    end = current_len
                    if " ".join(s.split(" ")[start:end]) != text:
                        print(i, text, " ".join(s.split(" ")[start:end]), s)
                    # word, position, pos, sentence, synset
                    sense_annotations.append({'id': word.attrib['id'], 'word': text, 'start': start, 'end': end, 'sense': gold[word.attrib['id']], 'lemma': word.attrib['lemma'], 'pos': word.attrib['pos'], 'sentence': s})

    return sense_annotations

Path('data/jsonl').mkdir(exist_ok = True)

for dir in tqdm(directories):
    for r, d, f in os.walk(f'data/{dir}/'):
        for file in f:
            ext = os.path.splitext(f'data/{dir}/{file}')[1]
            if ext == '.xml':
                xml_file = f'data/{dir}/{file}'
            elif ext == '.txt':
                gold_file = f'data/{dir}/{file}'


    sense_annotations = parse_sense_data(xml_file, gold_file)

    with open(f'data/jsonl/{dir}.jsonl', 'w') as f:
        for entry in sense_annotations:
            json.dump(entry, f)
            f.write('\n')
    
