# Earlypay ElasticSearch Clustering

## 장기 보관 데이터 베이스, 타겟 데이터

> 기존 elarypay backend RDS 데이터 분리 보관 목적
> table size가 너무 크고, select 전용으로만 사용하게 될 과거 데이터

1. platform sales


## Getting Start

> https://elasticsearch-py.readthedocs.io/
> https://sunscrapers.com/blog/how-to-use-elasticsearch-with-django/


## ENV 

1. `node.name=es-node1`: Specifies the name of the Elasticsearch node.
2. `discovery.seed_hosts=es1,es2`: Lists the seed hosts that the node will use for cluster discovery. This helps nodes find and join the cluster.
3. `cluster.initial_master_nodes=es-node0,es-node1,es-node2`: Specifies the initial master nodes in the cluster. It helps bootstrap the cluster formation.
4. `cluster.name=docker-cluster`: Sets the name of the Elasticsearch cluster.
5. `bootstrap.memory_lock=true`: Enables memory locking to prevent Elasticsearch from swapping memory to disk.
6. `"ES_JAVA_OPTS=-Xms512m -Xmx512m"`: Sets the JVM options for Elasticsearch, specifying the minimum and maximum heap sizes.
