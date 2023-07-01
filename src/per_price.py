from elasticsearch import Elasticsearch


es = Elasticsearch(
    hosts="https://localhost:9200",
    ca_certs="../certs/ca/ca.crt",
    basic_auth=("elastic", "admin123!"),
)

result = es.search(...)
res = es.index(index="platform_per_price", document=result)

# batch
# ubuntu