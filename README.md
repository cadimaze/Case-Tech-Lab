# CRUD Lab

Ferramenta educacional e interativa para aprender as quatro operações fundamentais de banco de dados — **Create, Read, Update, Delete** — através de uma API REST real.

O estudante preenche formulários, observa a **requisição HTTP sendo montada em tempo real**, envia para a API e vê a **resposta do servidor** com explicações didáticas de cada código de status.

🌐 **Demo ao vivo:** [crud-lab.vercel.app](https://crud-lab.vercel.app)

---

## O que o projeto ensina

- O que é CRUD e como cada operação mapeia para um método HTTP
- Como montar uma requisição HTTP (método, URL, headers, body JSON)
- O que significam os códigos de status HTTP (200, 201, 404, 409, 422…)
- Como ler e interpretar a resposta de uma API REST
- Diferença entre `PUT` (substituição completa) e `PATCH` (atualização parcial)
- Por que o `GET` e o `DELETE` não têm corpo na requisição

---

## Funcionalidades

| Recurso | Descrição |
|---|---|
| **Inspetor HTTP ao vivo** | Mostra a requisição completa (método, URL, headers, body) sendo construída enquanto o usuário preenche o formulário |
| **Painel de resposta** | Exibe o status HTTP e o corpo JSON da resposta com syntax highlighting |
| **Explicações de erro** | Cada código de erro (404, 409, 422…) exibe uma explicação didática do motivo |
| **Log da sessão** | Histórico de todas as requisições realizadas com método, URL, status e tempo |
| **Banco em tempo real** | Tabela que reflete o estado atual do banco após cada operação |
| **Modo demonstração** | Mock API completa em JavaScript — funciona sem servidor, dados isolados por sessão |
| **Fade-in de página** | Animação suave ao carregar o site |
| **Navegação sticky** | Barra de navegação fixa com atalhos para cada seção CRUD |

---

## Tecnologias

**Backend**
- Python 3.12
- FastAPI
- Pydantic v2
- Uvicorn

**Frontend**
- HTML5 + CSS3 + Vanilla JavaScript
- Fonte [Space Grotesk](https://fonts.google.com/specimen/Space+Grotesk) (Google Fonts)
- Mock API implementada em JavaScript (sem dependências externas)

**Deploy**
- [Vercel](https://vercel.com) — site estático servido pela pasta `static/`

---

## Estrutura do Projeto

```
Case-Tech-Lab/
├── static/
│   └── index.html       # Frontend completo (SPA com mock API embutida)
├── main.py              # Aplicação FastAPI com endpoints CRUD
├── models.py            # Modelos Pydantic com validações
├── requirements.txt     # Dependências Python
├── vercel.json          # Configuração de deploy no Vercel
└── README.md
```

---

## Modos de Funcionamento

### Modo Demonstração (padrão — Vercel e Live Server)

Quando acessado em qualquer host que **não seja** `127.0.0.1:8000`, o site opera com uma **mock API em JavaScript** que roda inteiramente no navegador:

- Banco de dados em memória (array JavaScript)
- Mesma lógica de validação do backend Python (incluindo CPF pelo algoritmo Mod 11)
- Mesmos endpoints, mesmos status codes, mesmas mensagens de erro
- **Dados isolados por sessão** — cada usuário começa com o banco vazio e os dados somem ao recarregar a página

### Modo API Real (desenvolvimento local)

Quando acessado em `http://127.0.0.1:8000` (servidor uvicorn rodando), o frontend faz chamadas HTTP reais para o backend FastAPI.

---

## Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/cadimaze/Case-Tech-Lab.git
cd Case-Tech-Lab
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie o servidor

```bash
uvicorn main:app --reload
```

Acesse em `http://127.0.0.1:8000`

> **Dica:** Também é possível abrir `static/index.html` pelo Live Server do VS Code (porta 5500) — o frontend detecta automaticamente e usa o modo demonstração.

---

## Endpoints da API

| Método | Rota | Status | Descrição |
|---|---|---|---|
| `POST` | `/pessoas/` | 201 | Cadastra uma nova pessoa |
| `GET` | `/pessoas/` | 200 | Lista todas as pessoas |
| `GET` | `/pessoas/{cpf}` | 200 | Retorna uma pessoa pelo CPF |
| `PUT` | `/pessoas/{cpf}` | 200 | Substitui completamente os dados de uma pessoa |
| `DELETE` | `/pessoas/{cpf}` | 200 | Remove uma pessoa pelo CPF |

Documentação interativa disponível em `http://127.0.0.1:8000/docs` (Swagger UI) e `/redoc`.

---

## Validações

| Campo | Regra |
|---|---|
| `nome_completo` | Entre 3 e 150 caracteres |
| `cpf` | 11 dígitos, aceita com ou sem formatação, validado pelo algoritmo Mod 11 |
| `data_nascimento` | Data no passado |
| `endereco` | Mínimo de 5 caracteres |
| `estado_civil` | `solteiro(a)`, `casado(a)`, `divorciado(a)`, `viúvo(a)`, `separado(a)`, `união estável` |

---

## Licença

[MIT](LICENSE.md)
