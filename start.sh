#!/bin/bash
echo ">> Elasticsearch And Kibana Project Docker Compose Init"
docker compose -f docker-compose.yml -p ek-docker-app stop
docker compose -f docker-compose.yml -p ek-docker-app down
docker compose -f docker-compose.yml -p ek-docker-app up -d
