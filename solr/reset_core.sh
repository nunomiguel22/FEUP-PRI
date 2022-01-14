#!/bin/bash

docker exec pri_solr bin/solr delete -c wines
docker exec pri_solr bin/solr create_core -c wines

docker cp stopwords.txt pri_solr:/var/solr/data/wines/conf

curl -X POST -H 'Content-type:application/json' \
--data-binary @schema.json \
http://localhost:8983/solr/wines/schema

curl 'http://localhost:8983/solr/wines/update?commit=true&f.note.split=true&f.note.separator=%7D' --data-binary @../datasets/vivino_reviews_final.csv -H 'Content-type:application/csv'
