import time
import json


# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('-f1', '--fname1')
# parser.add_argument('-f2', '--fname2')
# args = parser.parse_args()
#
# fname1 = args.fname1
# fname2 = args.fname2


data = [
   'Books',
   'Electronics',
   'Movies and TV',
   'CDs and Vinyl',
   'Clothing, Shoes and Jewelry',
   'Home and Kitchen',
   'Kindle Store',
   'Sports and Outdoors',
   'Cell Phones and Accessories',
   'Toys and Games',
   'Video Games',
   'Tools and Home Improvement',
   'Beauty',
   'Automotive',
   'Musical Instruments',
   'Digital Music',
   'Pet Supplies',
   'Patio, Lawn and Garden',
   'Grocery and Gourmet Food'
]

year_set = set([str(i) for i in range(2010, 2014)])


def read_data(d):
   for k, v in d.items():
      yield v


def write_json_file(total_md, fname):
   with open(f'result/merged_{fname}json', 'w') as f:
      for rd in read_data(total_md):
         f.write(json.dumps(rd))
         f.write("\n")


for name in data:
   print("write "+ name)
   total_md = {}
   st_time = time.time()
   with open(f'2014/{name}.json', 'r') as f:
       for d in f:
          d = json.loads(d, encoding='utf8')
          # if d['reviewTime'].split(",")[1].strip() in year_set:
          key = d['asin'] + d['reviewerID'] + d['reviewText']
          total_md[key] = d

   print('2014', len(total_md))

   key_set = set(total_md.keys())
   print('read 2018 data')
   with open(f'2018/{name}.json', 'r') as f:
       for d in f:
           d = json.loads(d, encoding='utf8')
           if 'reviewText' not in d.keys():
               continue
           key = d['asin'] + d['reviewerID'] + d['reviewText']
           tmp = {}

           # if key in key_set and d['reviewTime'].split(", ")[1].strip() in year_set:
           if key in key_set:
              tmp = total_md[key]
              tmp['asin'] = d['asin']
              tmp['reviewerID'] = d['reviewerID']
              if 'image' in d.keys():
                 tmp['image'] = d['image']
              if 'vote' in d.keys():
                 tmp['vote'] = d['vote']
              tmp['verified'] = d['verified']
              tmp['reviewTime'] = d['reviewTime']
              if 'style' in d.keys():
                 tmp['style'] = d['style']
              if 'reviewName' in d.keys():
                 tmp['reviewName'] = d['reviewName']
              if 'summary' in d.keys():
                 tmp['summary'] = d['summary']
              if 'unixReviewTime' in d.keys():
                 tmp['unixReviewTime'] = d['unixReviewTime']
              tmp['reviewText'] = d['reviewText']
              total_md[key] = tmp

   print('2014', len(total_md))
   ed_time = time.time()
   print(ed_time-st_time)
   write_json_file(total_md, name)



# import json
# import pandas as pd
# import time
# for d in data:
#    print('concat from (1996, 2014)', d)
#    s_time = time.time()
#    df1 = pd.read_json(f"2014/{d}.json", lines=True)
#    df1 = pd.read_json(df1['reviewTime'].str.split(", ").str[1] in range(1996, 2014))
#    df2 = pd.read_json(f"2018/{d}.json", lines=True)
#    df2 = pd.read_json(df2['reviewTime'].str.split(", ").str[1] in range(1996, 2014))
#    result = pd.concat([df1, df2], axis=1, join='inner')
#    result.to_json(f'result_{f1}_{f2}.json')
#    e_time = time.time()
#    print(e_time-s_time)


