#!/bin/bash

# 因为 -v 参数不支持相对路径，在本地具体环境中需修改本地文件路径地址

docker run -e ES_JAVA_OPTS="-Xms256m -Xmx256m" --rm --name es-single -p 9200:9200 -p 9300:9300 -v /Users/shiqiang/Projects/2024-projects/code-space/docker-conf/single-es/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml -d docker.elastic.co/elasticsearch/elasticsearch:6.3.1
