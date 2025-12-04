# EJ RHAI Platform

Plataforma de recrutamento e análise de recursos humanos com interface web moderna e backend Flask.

## 📋 Requisitos

- Python 3.7+
- Flask

## 🚀 Instalação e Execução

### 1. Instalar dependências

```bash
pip install Flask
```

### 2. Executar o servidor

```bash
python app.py
```

O servidor iniciará em `http://127.0.0.1:5000`

### 3. Acessar a aplicação

Abra seu navegador e acesse: `http://127.0.0.1:5000`

## 📁 Estrutura do Projeto

```
platform-ejrhai/
├── index.html       # Frontend SPA (HTML + CSS + JavaScript)
├── app.py          # Backend Flask com APIs mock
└── README.md       # Este arquivo
```

## 🎯 Funcionalidades

### Frontend (index.html)

- **Tela Inicial:** Duas cartas para navegação (Alunos & Adultos / Empresas)
- **Menu Hamburger:** Flutuante com animação suave
- **Busca e Contratação:** 
  - Grid de perfis com 12+ candidatos
  - Filtros avançados (idade, área, cidade, escola)
  - Modais para visualizar perfil e contratar
- **EJ RHAI:**
  - Recomendações de candidatos por descrição de vaga
  - Análise de desempenho com gráficos (hard skills / soft skills)
  - Calculadora de métricas de RH
- **Google Drive:** Link direto para pasta compartilhada (configurável)
- **Design:** Profissional, moderno, preto/branco/cinza + verde escuro
- **Responsivo:** Funciona em desktop, tablet e mobile

### Backend (app.py)

#### Endpoints de API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/profiles` | Lista todos os perfis |
| GET | `/api/profile/<id>` | Retorna perfil detalhado |
| POST | `/api/search` | Busca com filtros |
| POST | `/api/hire` | Registra contratação |
| POST | `/api/ejrhai/recommend` | Recomenda candidatos |
| POST | `/api/ejrhai/calc` | Realiza cálculos |
| GET | `/api/ejrhai/analytics` | Retorna analytics |

#### Dados Mock

- 12 perfis de candidatos com dados realistas
- Scores de hard skills e soft skills
- Dados armazenados em memória (sem persistência)

## 🎨 Paleta de Cores

```css
--black: #000000
--white: #FFFFFF
--gray-100: #f4f4f4
--gray-500: #7a7a7a
--gray-800: #2b2b2b
--dark-green: #0b3d2e (destaque)
```

## 🔧 Configuração do Google Drive

Para usar um link real do Google Drive:

1. Abra `index.html` em um editor de texto
2. Procure por: `const GOOGLE_DRIVE_URL = `
3. Substitua o valor por seu link compartilhado:
   ```javascript
   const GOOGLE_DRIVE_URL = 'https://drive.google.com/drive/folders/SEU_ID_AQUI';
   ```

## 📱 Responsividade

A aplicação é totalmente responsiva:

- **Desktop:** Layout completo com menu lateral flutuante
- **Tablet:** Grid adaptativo, menu hamburger
- **Mobile:** Layout vertical, menu hamburger, botões otimizados

## 🚦 Fluxo de Uso

1. **Home:** Clique em "Empresas" para acessar a área de recrutamento
2. **Busca:** Veja todos os candidatos ou use filtros
3. **Perfil:** Clique em "Ver Perfil" para detalhes completos
4. **Contratação:** Clique em "Contratar" e insira o nome da empresa
5. **EJ RHAI:** Use o menu para acessar recomendações, análises e calculadora

## 💡 Exemplos de Uso

### Buscar por especialização

1. Clique em "Filtros"
2. (Nota: Busca por especialização está integrada na busca de texto)
3. Digite "Python" ou "React" na barra de busca
4. Clique em "Buscar"

### Obter recomendações

1. Acesse "EJ RHAI" pelo menu
2. Clique na aba "Recomendações"
3. Descreva a vaga (ex: "Desenvolvedor Python senior com AWS")
4. Clique em "Obter Recomendações"

### Ver análises

1. Acesse "EJ RHAI" pelo menu
2. Clique na aba "Análise de Funcionários"
3. Visualize gráficos de hard skills e soft skills por área

## 🔐 Segurança

- Aplicação mock sem autenticação (para desenvolvimento)
- Dados em memória (não persistem após reinicialização)
- CORS habilitado para requisições locais

## 📝 Notas

- A aplicação é totalmente funcional sem conexão com banco de dados externo
- Todos os dados são simulados e resetam ao reiniciar o servidor
- Ideal para prototipagem e demonstração
- Preparada para upgrade futuro com banco de dados real

## 🤝 Contribuições

Este é um projeto de demonstração. Para melhorias ou sugestões, abra uma issue no GitHub.

## 📄 Licença

MIT

---

**Desenvolvido com ❤️ para EJ RHAI Platform**
