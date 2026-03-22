# 📊 Projeto 1: Extrator e Saneamento de Dados com Python & Pandas

Este repositório faz parte da minha trilha de estudos em **Engenharia de Dados**, focada em consolidar conhecimentos práticos de ETL (Extraction, Transformation, and Loading) e manipulação de dados.

## 📝 Sobre o Projeto
O objetivo deste projeto foi simular um cenário real de tratamento de dados de saúde. A partir de um conjunto de dados brutos (fictícios) com inconsistências, utilizei a biblioteca **Pandas** para realizar a limpeza e padronização, garantindo a integridade da informação para futuras análises.

## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **Pandas**: Manipulação e análise de dados.
* **NumPy**: Suporte para valores matemáticos e nulos (NaN).

## 🔍 Etapas do Processo (Pipeline)

1. **Extração**: Simulação de carga de dados brutos em um DataFrame.
2. **Transformação (Data Cleaning)**:
    - Remoção de registros duplicados.
    - Tratamento de valores nulos (Eliminação de registros sem identificação de paciente).
    - Aplicação de regras de negócio (Correção de idades negativas para zero).
    - Padronização de strings (Capitalização de cidades e nomes de doses).
    - Conversão de tipos (Transformação de strings em objetos de Data).
    - Enriquecimento de dados (Criação da coluna de país).
3. **Carregamento**: Exportação dos dados limpos para um arquivo `.csv` pronto para consumo.

## 🚀 Como executar o projeto
1. Clone o repositório:
```bash
  git clone https://github.com/TaisPrates/estudos-engenharia-dados.git
```
2. Instale as dependências:
```bash
pip install pandas numpy
```
3. Execute o script:
```bash
pipeline_de_limpeza_e_padronização_de_dados.py
```
