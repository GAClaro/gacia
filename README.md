# GACIA

**GACIA (Generative AI Corporate Information Assistant)** é um projeto de
assistente corporativo baseado em inteligência artificial e recuperação de
informações a partir de documentos empresariais.

O projeto tem como objetivo explorar a construção de um SaaS capaz de
responder perguntas utilizando uma base de conhecimento fornecida pela
empresa, evitando respostas baseadas exclusivamente no conhecimento geral
do modelo de linguagem.

O projeto foi feito para o Oracle Next Education, com apoio da Alura cursos, 
Turma G10, para o prosseguimento do Tech AI Builder.
GACIA é fictício, adaptação das iniciais do meu nome com inteligência artificial, que gerou o nome acrônimo acima 

> **Status:** MVP em desenvolvimento. Encerrado nesta parte para o desafio Alura One.

---

## Sobre o projeto

O GACIA foi desenvolvido como um projeto experimental de SaaS utilizando
inteligência artificial generativa.

A proposta é permitir que uma empresa disponibilize documentos internos,
como:

- FAQs;
- políticas;
- manuais;
- tabelas de preços;
- documentos institucionais;
- contratos;
- planilhas;
- outros documentos corporativos.

O usuário pode fazer perguntas em linguagem natural e o sistema utiliza o
Google Gemini com File Search para localizar informações relevantes na base
de conhecimento antes de gerar a resposta.

---

## Funcionalidades atuais

- Interface web para perguntas e respostas;
- Integração com Google Gemini API;
- Utilização do Gemini File Search;
- Busca baseada em documentos;
- Respostas fundamentadas na base de conhecimento;
- Instruções para evitar respostas fora dos documentos;
- Tratamento básico de informações não encontradas;
- Suporte a diferentes formatos de documentos;
- API HTTP desenvolvida com FastAPI.

---

## Arquitetura

A versão atual utiliza uma arquitetura simples:

```text
Usuário
   │
   ▼
Interface Web
   │
   ▼
FastAPI
   │
   ▼
GACIA Agent
   │
   ▼
Google Gemini
   │
   ▼
File Search
   │
   ▼
Base de documentos

## Tecnologias

# Backend
* Python
* FastAPI
* Uvicorn

# Inteligência Artificial
* Google Gemini API
* Gemini File Search

# Frontend
*HTML
*CSS
*JavaScript

# Dados
* Markdown
* CSV
* JSON
* PDF
* DOCX
* XLSX

# Infraestrutura
* Git
* GitHub
* Oracle Cloud Infrastructure (OCI)

## Estrutura do projeto

gacia/
│
├── app/
│   ├── agent.py
│   ├── documents.py
│   ├── gemini.py
│   ├── knowledge.py
│   ├── main.py
│   ├── setup_knowledge.py
│   ├── test_agent.py
│   ├── test_file_search.py
│   └── test_gemini.py
│
├── documents/
│   └── Base de conhecimento
│
├── static/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

## 1. Instruções para executar o projeto

### Pré-requisitos

- Python 3.11 ou superior
- Uma chave da API do Google Gemini
- Um File Search Store configurado no Google Gemini
- Git (opcional, caso o projeto seja obtido pelo GitHub)

### Clonar o projeto

```bash
git clone https://github.com/GAClaro/gacia.git
cd gacia
```

### Criar o ambiente virtual

No Git Bash:

```bash
python -m venv .venv
```

### Ativar o ambiente virtual

No Git Bash:

```bash
source .venv/Scripts/activate
```

No Windows CMD:

```cmd
.venv\Scripts\activate
```

### Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### Configurar as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
GEMINI_API_KEY=SUA_CHAVE_DA_API
FILE_SEARCH_STORE_NAME=fileSearchStores/SEU_STORE
```

**Nunca publique a chave da API no GitHub.** O arquivo `.env` deve permanecer fora do controle de versão.

### Executar a aplicação

Com o ambiente virtual ativado:

```bash
python -m uvicorn app.main:app --reload
```

A aplicação estará disponível em:

```text
http://127.0.0.1:8000
```

Abra esse endereço no navegador para utilizar a interface do GACIA.

### Executar os testes do agente

```bash
python -m app.test_agent
```

Também estão disponíveis testes para os componentes de Gemini e File Search:

```bash
python -m app.test_gemini
python -m app.test_file_search
```

## 2. Estrutura básica do projeto

```text
gacia/
├── app/
│   ├── agent.py
│   ├── documents.py
│   ├── gemini.py
│   ├── knowledge.py
│   ├── main.py
│   ├── setup_knowledge.py
│   ├── test_agent.py
│   ├── test_file_search.py
│   └── test_gemini.py
│
├── documents/
│   └── Base de conhecimento
│
├── static/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## 3. Exemplos de perguntas e respostas

As respostas abaixo são exemplos baseados na base de conhecimento fictícia utilizada no projeto.

### Exemplo 1 — Planos e API

**Pergunta:**

> Quais planos possuem acesso à API?

**Resposta esperada:**

> Os planos que possuem acesso à API são o **Professional** e o **Enterprise**. O plano Starter não possui acesso a esse recurso.

---

### Exemplo 2 — Número de usuários

**Pergunta:**

> Quantos usuários estão incluídos no plano Enterprise?

**Resposta esperada:**

> O plano Enterprise inclui até **100 usuários**.

---

### Exemplo 3 — Reembolso

**Pergunta:**

> Qual é o prazo para solicitar reembolso de uma assinatura anual?

**Resposta esperada:**

> Clientes que contrataram um plano anual podem solicitar reembolso em até **7 dias corridos após a contratação**, observadas as condições previstas na política de reembolso.

---

### Exemplo 4 — Período de teste

**Pergunta:**

> Quantos dias dura o período de teste?

**Resposta esperada:**

> O período de teste gratuito é de **14 dias**.

---

### Exemplo 5 — Manual

**Pergunta:**

> Como adiciono um novo usuário na NexaCloud?

**Resposta esperada:**

> Um usuário com permissão administrativa deve acessar **Configurações > Equipe > Adicionar usuário**, informar o nome e o e-mail, escolher o nível de acesso e enviar o convite.

---

### Exemplo 6 — Informação não encontrada

**Pergunta:**

> Qual é o salário médio dos funcionários da NexaTech?

**Resposta esperada:**

> Não encontrei essa informação nos documentos disponíveis.

Esse último teste é especialmente importante: o GACIA deve evitar inventar informações quando a base de conhecimento não contém uma resposta suficiente.

## 4. Funcionamento resumido

```text
Usuário
   ↓
Interface Web
   ↓
FastAPI
   ↓
GACIA Agent
   ↓
Google Gemini
   ↓
File Search
   ↓
Documentos da empresa
```

O agente recebe a pergunta, consulta a base de conhecimento por meio do File Search e utiliza as informações encontradas para produzir a resposta.

## 5. Segurança

A chave da API deve ser armazenada exclusivamente em variáveis de ambiente ou em um arquivo `.env` que não seja enviado ao GitHub.

Não coloque credenciais, chaves de API ou informações privadas de clientes nos arquivos versionados do projeto.

## 6. Roadmap

- [x] Estrutura inicial do projeto
- [x] Integração com Google Gemini
- [x] Integração com File Search
- [x] Agente de perguntas e respostas
- [x] Interface web
- [x] Base inicial de documentos
- [x] Repositório GitHub
- [x] Testes com diferentes formatos de documentos
- [x] Deploy na Oracle Cloud Infrastructure (OCI)
- [x] Upload de documentos pela interface
- [ ] Autenticação de usuários
- [ ] Histórico de perguntas
- [ ] Gerenciamento de documentos
- [ ] Separação de bases por empresa
- [ ] Dashboard administrativo


## Status

## Autor

# Guilherme de Almeida Claro
Projeto independente de desenvolvimento de SaaS e exploração de aplicações
de inteligência artificial generativa, realizado para o Desafio Alura do Programa TECH AI BUILDER.

