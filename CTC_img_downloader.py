import urllib.request
import json
import os
from tqdm import tqdm

with open ('CTC_anns.json', 'r') as fp:
    ctc_anns = json.load(fp)

os.mkdir('./images/')

for item in tqdm(ctc_anns['images']):
    urllib.request.urlretrieve(item['coco_url'], './images/'+ item['coco_url'].strip().split('/')[-1])

