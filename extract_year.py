import json
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('-y', '--year')
parser.add_argument('-f', '--fname')
args = parser.parse_args()

# year = args.year
fname = args.fname


def extract_year_data(years):
    with open(fname, 'r') as f:
        for d in f:
            d = json.loads(d, encoding='utf8')
            if 'reviewText' not in d.keys():
                continue
            if d['reviewTime'].split(', ')[1] in years:
                yield d


def extract_year():
    filename = fname.split("/")[-1].split(".")[0]
    years = set([str(i) for i in range(2010, 2014)])
    with open(f'result/year_{filename}.json', 'w') as f:
        for d in extract_year_data(years):
            f.write(json.dumps(d))
            f.write("\n")

extract_year()





