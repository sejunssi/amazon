import time
import json

data = ['all']

def read_data(d):
   for k, v in d.items():
      yield v


def write_json_file(total_md, fname):
   with open(f'result/merged_{fname}.json', 'w') as f:
      for rd in read_data(total_md):
         f.write(json.dumps(rd))
         f.write("\n")


for name in data:
   print("write "+ name)
   total_md = {}
   st_time = time.time()
   with open(f'2014/year_{name}.json', 'r') as f:
       for d in f:
          d = json.loads(d, encoding='utf8')
          # if d['reviewTime'].split(",")[1].strip() in year_set:
          key = d['asin'] + d['reviewerID'] + d['reviewText']
          total_md[key] = []
          total_md[key] = d

   print('2014', len(total_md))

   key_set = set(total_md.keys())
   print('read 2018 data')
   with open(f'2018/year_{name}.json', 'r') as f:
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
              tmp['reviewText'] = d['reviewText']
              if 'image' in d.keys():
                 tmp['image'] = d['image']
              if 'vote' in d.keys():
                 tmp['vote'] = d['vote']
              if 'vote' in d.keys():
                 tmp['vote'] = d['vote']
              if 'reviewTime' in d.keys():
                 tmp['reviewTime'] = d['reviewTime']
              if 'style' in d.keys():
                 tmp['style'] = d['style']
              if 'reviewName' in d.keys():
                 tmp['reviewName'] = d['reviewName']
              if 'summary' in d.keys():
                 tmp['summary'] = d['summary']
              if 'unixReviewTime' in d.keys():
                 tmp['unixReviewTime'] = d['unixReviewTime']
              total_md[key] = tmp

   print('2014', len(total_md))
   ed_time = time.time()
   print(ed_time-st_time)
   write_json_file(total_md, name)






