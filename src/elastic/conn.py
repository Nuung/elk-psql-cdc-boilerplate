from elasticsearch import Elasticsearch

class ElasticGateway:
    
    def __init__(self) -> None:
        es = Elasticsearch(
            hosts="https://localhost:9200",
            ca_certs="../certs/ca/ca.crt",
            basic_auth=("elastic", "admin123!"),
        )
        
        
    def _check_status(self) -> None:
        print(self.es.info())