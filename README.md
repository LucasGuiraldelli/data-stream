# Projeto: stream-api-kafka-airflow

## Descrição

Este projeto é a primeira etapa de um pipeline de dados em tempo real. Ele utiliza o Apache Airflow para orquestrar, a cada 5 segundos, a coleta de dados de uma API pública (CoinDesk - cotação do Bitcoin) e envia essas informações como eventos para um tópico Kafka.

Essa arquitetura simula um sistema de ingestão contínua, como em um cenário de dados transacionais, preparando terreno para processamento com Spark e validações futuras.

---

## Tecnologias Utilizadas

- Apache Kafka
- Zookeeper
- Apache Airflow
- Python 3
- Docker + Docker Compose
- Kafka-Python
- API CoinDesk

---

## Como Executar

### Pré-requisitos

- Docker Desktop instalado e rodando (com suporte a WSL2)
- Python 3.10+ com pip
- VS Code ou outro editor

### Instale as dependencias

pip install kafka-python requests


### Acesse o airflow:   http://localhost:8080

Login padrão: airflow / airflow

Ative a DAG coleta_api_para_kafka.
