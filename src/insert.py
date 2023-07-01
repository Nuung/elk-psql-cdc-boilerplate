import csv
from typing import List, Dict
from datetime import datetime

from elasticsearch import Elasticsearch
from dateutil import parser


def data_processing(data: Dict) -> Dict:
    
    processed_data = dict()
    for k, v in data.items():
        if k in ["amount_sale", "amount_fee", "amount_deposit"]:
            try:
                processed_data[k] = int(v)
            except Exception:
                processed_data[k] = None
        elif k == "is_canceled":
            processed_data[k] = bool(v)
        elif k in ["created", "modified", "sold_at"]:
            processed_data[k] = parser.isoparse(v)
        elif k == "raw_data":
            continue
        else:
            processed_data[k] = v
    return processed_data

def get_csv_dict(file_path: str) -> List[Dict]:
    data_dict = []
    with open(file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data_dict.append(data_processing(row))
    return data_dict

def test_csv_to_datamodel():
    file_path = f"./platform_sales/platform_sales_300.csv"
    docs = get_csv_dict(file_path)
    print(docs[0])

# test_csv_to_datamodel()

es = Elasticsearch(
    hosts="https://localhost:9200",
    ca_certs="../certs/ca/ca.crt",
    basic_auth=("elastic", "admin123!"),
)
print(es.info())

for i in range(10, 100):
    file_path = f"./platform_sales/platform_sales_3{i}.csv"
    docs = get_csv_dict(file_path)
    
    if i % 5 == 0:
        print(i, file_path, "turn..")

    for doc in docs:
        doc["timestamp"] = datetime.now()
        res = es.index(index="platform_sales", document=doc)


# # search 
# query = {
#     "match": {
#         "content": "example"
#     }
# }
# response = es.search(index=index_name, query=query)
# print(response)

# # delete
# response = es.indices.delete(index="platform_sales")
# print(response)