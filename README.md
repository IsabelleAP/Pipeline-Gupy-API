# ANÁLISE DE DADOS - VAGAS DE DADOS NA GUPY

## 📌 Pipeline Gupy API
Este projeto implementa um pipeline de coleta e análise de vagas de emprego utilizando a API pública da Gupy. Ele integra Python, manipulação de dados, integração com API, análise exploratória e visualização em Power BI.

### Objetivos
* Consumir a API Gupy para buscar vagas com base em palavras-chave.
* Aermazenar os resultados em arquivos JSON organizados.
* Análise exploratória em Python
* Dashboard no Power BI

### Tecnologias Utilizadas
* Python (requests, pandas, json) - comunicação com a API da Gupy e manipulação e análise de dados
* API REST da Gupy
* Power BI
* Jupyter Notebook

### Estrutura do projeto
```
Pipeline-Gupy-API
│── src/
│   ├── api.py        # Funções para consumir a API
│   ├── storage.py    # Funções para salvar arquivos
│   └── main.py       # Fluxo principal do pipeline
│── dados/
│   └── vagas/        # Arquivos JSON gerados
│── notebook/         # Notebooks exploratórios
│── powerbi/          # Dashboard simples em Power BI
│── requeriments.txt  # Dependências do projeto
│── README.md         # Documentação

```

### Como executar
1. Clone o repositório 
```bash
git clone https://github.com/IsabelleAP/Pipeline-Gupy-API.git
```
2. Instale as dependências:
```bash
pip install -r requeriments.txt
```
3. Execute o pipeline:
```bash
python3 src/main.py
```
Os arquivos JSON serão gerados em `dados/vagas`.

### API utilizada
https://portal.api.gupy.io/api/job
