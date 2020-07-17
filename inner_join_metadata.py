import ast
import json
import argparse
import os.path
from os import path

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f', '--fname')
args = parser.parse_args()

fname = args.fname

def read_data(fname):
    with open(f'./merged_{fname}.json', 'r') as f:
        for d in f:
            d = json.loads(d, encoding='utf8')
            yield d


def merged_metadata(fname):
    print("write merged metadata")
    md_data = {}
    with open(f'metadata.json', 'r') as f:
        for d in f:
            d = ast.literal_eval(d)
            md_data[d['asin']] = d
    md_data_set = set(md_data[d['asin']])
    with open(f'merged_metadata_{fname}.json', 'w') as f:
        for d in read_data(fname):
            if d['asin'] in md_data_set:
                for k, v in md_data_set[d['asin']]:
                    d[k] = v
                    f.write(json.dumps(d))

    if path.exists(f"./{d['categories']}"):
        with open(f'./categories/{d["categories"]}/final_{fname}.json', 'w') as f2:
            for d in read_data(fname):
                if 'categories' in d.keys() and d['asin'] in md_data_set:
                    for k, v in md_data_set[d['asin']]:
                        d[k] = v
                        f2.write(json.dumps(d))
    else:
        os.mkdir(f'./{d["categories"]}')
        with open(f'./categories/{d["categories"]}/final_{fname}.json', 'w') as f2:
            for d in read_data(fname):
                if 'categories' in d.keys() and d['asin'] in md_data_set:
                    for k, v in md_data_set[d['asin']]:
                        d[k] = v
                        f2.write(json.dumps(d))
merged_metadata(fname)


# import pandas as pd
# import time
#
# def merged_data(fname):
#    print('concat merge metadata')
#    s_time = time.time()
#    df1 = pd.read_json(f"{fname}.json", lines=True)
#    df2 = pd.read_json(f"metadata.json", lines=True)
#    result = pd.concat([df1, df2], axis=1, join='inner')
#    result.to_json(f'merged_metadata_{fname}.json')
#    e_time = time.time()
#    print(e_time-s_time)
#
# merged_data(fname1)
