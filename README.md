# Blog sobre Python

Este é um projeto de um blog simples desenvolvido em Flask, que exibe posts sobre Python. O blog lê dados de um arquivo JSON e renderiza as informações em páginas HTML.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada.
- **Flask**: Framework web leve para desenvolvimento de aplicações em Python.
- **HTML/CSS**: Para a estruturação e estilização das páginas web.
- **JSON**: Formato utilizado para armazenar os dados dos posts.

## Estrutura do Projeto

```plaintext
.
├── data
│   └── data.json      # Arquivo JSON contendo os dados dos posts
├── static
│   └── css
│       └── styles.css # Folhas de estilo CSS
├── templates
│   ├── index.html     # Página inicial que lista todos os posts
│   └── post.html      # Página para exibir um post específico
├── main.py             # Arquivo principal da aplicação
├── post.py            # Módulo contendo a classe Post
├── server.py            # Arquivo contendo a lógica de rotas
└── utils.py           # Módulo com funções utilitárias
```

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/iagooteles/blogPython.git
cd nome_do_repositorio
```

2. Crie um ambiente virtual (opcional, porém recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux ou macOS
venv\Scripts\activate  # Windows
```

3. Instale as dependências

```bash
pip install
```

### Uso

1. Inicie o servidor:
```bash
python main.py

```

2. Acesse a aplicação:
Abra seu navegador e vá para http://127.0.0.1:5000 para ver a lista de posts.

