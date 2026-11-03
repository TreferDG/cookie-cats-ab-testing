# 🎮 Game Analytics & Teste A/B: O Impacto do Churn no Cookie Cats

**Análise de retenção de usuários e testes A/B em jogos mobile utilizando Python, MySQL e Power BI.**

---

## 📋 Sobre o Projeto

Este projeto simula um cenário real de **Game Analytics** utilizando o dataset do **Cookie Cats**, um popular jogo de puzzle para celular desenvolvido pela *Tactile Entertainment*.

O objetivo central é analisar o comportamento dos jogadores e avaliar o impacto de um **Teste A/B** estratégico: o reposicionamento do portão de tempo (*gate*) obrigatório do nível 30 (`gate_30`) para o nível 40 (`gate_40`). A métrica de sucesso principal é a **Retenção de Usuários (Day 1 e Day 7)** e o engajamento em número de rodadas jogadas (`sum_gamerounds`).

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python 3.14
* **Bibliotecas:** Pandas, SQLAlchemy, PyMySQL
* **Banco de Dados Relacional:** MySQL Local
* **Visualização de Dados:** Power BI
* **Controle de Versão:** Git & GitHub

---

## 📂 Estrutura do Repositório

```text
cookie-cats-ab-testing/
├── dados/                       # Dataset bruto (cookie_cats.csv) - ignorado via .gitignore
├── SQL/
│   ├── 01_validacao.sql         # Scripts de validação e qualidade dos dados
│   └── 02_metricas_retencao.sql # Queries para cálculo de taxas de retenção e engajamento
├── scripts/
│   └── pipeline_cookie_cats.py  # Script em Python para ingestão automatizada no MySQL
├── assets/                      # Imagens e prints do dashboard para o README
└── README.md                    # Documentação oficial do projeto
```

---

## 🔄 Passo a Passo da Execução

### 1. Configuração do Banco de Dados

No seu servidor MySQL local, crie o banco de dados dedicado ao projeto:

```sql
CREATE DATABASE cookie_cats_db;
```

### 2. Ingestão de Dados via Pipeline Python

O script em Python automatiza a leitura do arquivo CSV bruto e carrega os dados diretamente para o banco relacional MySQL:

* Tratamento de caminhos e codificação.
* Conexão segura via SQLAlchemy e PyMySQL.
* Carga estruturada na tabela `raw_cookie_cats`.

### 3. Validação e Qualidade dos Dados (`SQL/`)

Antes de gerar insights, foram executadas consultas SQL para:

* Validar a unicidade de cada `userid` (garantindo que não há duplicatas).
* Conferir a integridade contra valores nulos.
* Medir a distribuição volumétrica entre os grupos do teste A/B (`gate_30` vs `gate_40`), garantindo uma divisão equilibrada de aproximadamente 50/50.

### 4. Análise de Métricas de Negócio (`SQL/`)

Extração das principais métricas de produto:

* **Média de Rodadas:** quantas rodadas os usuários jogaram na primeira semana em cada grupo.
* **Taxa de Retenção Day 1 (D1):** percentual de jogadores que retornaram no dia seguinte à instalação.
* **Taxa de Retenção Day 7 (D7):** percentual de jogadores engajados após uma semana.

---

## 📊 Dashboard Executivo (Power BI)

> *(Em breve: imagem prévia do dashboard em Power BI)*

O dashboard consolida os principais indicadores para tomada de decisão de produto:

* **KPI Cards:** total de usuários, média geral de rodadas e taxas globais de retenção.
* **Comparativo A/B:** gráficos de barras lado a lado evidenciando a performance de retenção entre o grupo controle (`gate_30`) e o grupo de teste (`gate_40`).
* **Análise de Churn:** distribuição do abandono de jogadores por faixa de rodadas jogadas.

---

## 💡 Principais Insights de Negócio

A análise do teste A/B revelou que mover o portão do nível 30 para o nível 40 impacta diretamente a retenção de longo prazo (Day 7), demonstrando a sensibilidade dos jogadores de puzzle a barreiras precoces de progressão.

Os dados ajudam a responder à pergunta de produto:

> *"Forçar o jogador a esperar mais tempo para avançar gera mais receita a curto prazo ou afugenta a base de usuários?"*

---

## 🚀 Como Reproduzir o Projeto

1. Clone este repositório na sua máquina:

   ```bash
   git clone https://github.com/seu-usuario/cookie-cats-ab-testing.git
   ```

2. Baixe o dataset **Mobile Games A/B Testing & Churn** no Kaggle e coloque-o na pasta `dados/`.

3. Instale as dependências necessárias:

   ```bash
   pip install pandas sqlalchemy pymysql
   ```

4. Ajuste as credenciais do seu MySQL no arquivo `scripts/pipeline_cookie_cats.py` e execute o pipeline:

   ```bash
   python scripts/pipeline_cookie_cats.py
   ```

5. Utilize os scripts da pasta `SQL/` no MySQL Workbench para rodar as validações e o cálculo das métricas.

---

Feito com 💻 por **Danilo Guerreiro**.
