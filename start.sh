#!/bin/bash
echo ">> Init Elasticsearch, Kibana and Logstash Change Data Capcture from PSQL Project Docker Compose << "
docker compose -f docker-compose.yml -p elk-cdc-app stop
docker compose -f docker-compose.yml -p elk-cdc-app down
docker compose -f docker-compose.yml -p elk-cdc-app up -d

sleep 1

docker compose -p elk-cdc-app logs -f