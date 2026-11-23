<h1 align="center">Trilha de IA em português</h1>

<p align="center">
  <strong>Estudos de Inteligência Artificial em ordem, do básico a agentes e produção, com curadoria de cursos abertos de referência.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Conte%C3%BAdo-Markdown-083FA1?style=for-the-badge&logo=markdown&logoColor=white" alt="Conteúdo em Markdown" />
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12" />
  <img src="https://img.shields.io/badge/GitHub_Actions-Links-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/Licen%C3%A7a-MIT-green?style=for-the-badge" alt="Licença MIT" />
</p>

---

Uma trilha de estudos de Inteligência Artificial em ordem, do básico até agentes e produção, montada a partir de cursos abertos de referência. Cada etapa linka para a fonte original, indica o idioma e avisa quando há tradução para português do Brasil.

> [!NOTE]
> **O que este repositório é:** curadoria e ordenação. Não copia nem reescreve o conteúdo dos autores.
> **O que ele não é:** um curso novo nem uma tradução. O crédito de cada lição fica com quem a criou.

---

## Início Rápido

1. Leia [Como estudar](trilha/00-como-estudar.md).
2. Siga os módulos na ordem da tabela abaixo.
3. Em cada módulo, marque os itens conforme concluir. Para manter seu progresso, faça um fork.

## Mapa da trilha

| # | Módulo | O que você aprende |
|---|---|---|
| 1 | [Fundamentos de IA](trilha/01-fundamentos-de-ia.md) | Entender o que é IA, de onde veio e quais são as preocupações éticas, antes de entrar nas técnicas. |
| 2 | [Machine Learning clássico](trilha/02-machine-learning-classico.md) | Aprender o ciclo básico de ML (dados, treino, avaliação) com regressão, classificação, agrupamento, PLN, séries temporais e aprendizado por reforço. |
| 3 | [Redes neurais do zero](trilha/03-redes-neurais.md) | Construir a intuição de como redes neurais aprendem (backpropagation, ativações, gradientes) e implementar tudo de forma explícita. |
| 4 | [Visão computacional](trilha/04-visao-computacional.md) | Estudar como redes aprendem com imagens: convoluções, transfer learning, modelos generativos, detecção e segmentação. |
| 5 | [Linguagem natural e Transformers](trilha/05-linguagem-e-transformers.md) | Seguir a evolução da representação de texto, de TF-IDF até Transformers, e abrir a arquitetura que sustenta os LLMs. |
| 6 | [LLMs na prática](trilha/06-llms-na-pratica.md) | Usar e adaptar modelos de linguagem em tarefas reais: embeddings, classificação, prompts, geração, busca semântica e ajuste fino. |
| 7 | [RAG: recuperação e geração aumentada](trilha/07-rag.md) | Começar pelo RAG simples e ir adicionando técnicas de consulta, chunking, recuperação, avaliação e arquiteturas avançadas. |
| 8 | [Agentes de IA](trilha/08-agentes-de-ia.md) | Construir agentes que usam ferramentas, planejam, lembram, colaboram e podem ser levados a produção com segurança. |
| 9 | [ML em produção (MLOps)](trilha/09-ml-em-producao.md) | Sair do notebook: estruturar, testar, versionar, servir e implantar uma aplicação de ML com CI/CD. |
| 10 | [Tópicos extras](trilha/10-topicos-extras.md) | Ampliar o repertório com algoritmos genéticos, aprendizado por reforço profundo, sistemas multiagentes e redes multimodais. |

## Fontes

Sete repositórios abertos sustentam a trilha. Veja detalhes, licenças e data de conferência em [FONTES.md](FONTES.md).

## Princípios

- **Sem cópia:** nenhum arquivo, notebook, imagem ou texto dos autores é copiado para cá. Só links.
- **Sem invenção:** títulos e ordem partem da estrutura real dos repositórios. Quando uma indicação de pré-requisito aparece, ela vem do próprio material (e fica dito qual).
- **Crédito e licença:** autores e licenças estão em [FONTES.md](FONTES.md). Um dos materiais (RAG_Techniques) tem licença de uso não comercial, e a trilha avisa isso no módulo correspondente.
- **Links verificáveis:** existe um script e um workflow para conferir os links. Veja [Verificação de links](docs/verificacao-de-links.md).

## Status

Versão 0.1. Os links e a estrutura foram conferidos contra os repositórios de origem em 23/11/2026. Os notebooks não foram executados durante a curadoria. Se algo quebrar, abra uma issue.

---

## Estrutura Padrão do Projeto

Disposição das pastas e arquivos do repositório:

```text
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── link-quebrado.md          # Modelo de issue para link quebrado
│   │   └── sugerir-recurso.md        # Modelo de issue para sugerir recurso
│   ├── workflows/
│   │   └── links.yml                 # Verificação de links (PR, semanal e manual)
│   └── pull_request_template.md      # Modelo de pull request
├── docs/                             # Manuais de apoio
│   ├── README.md                     # Índice da documentação
│   └── verificacao-de-links.md       # Como o verificador de links funciona
├── scripts/
│   └── verificar_links.py            # Verificador de links (Python, sem dependências)
├── trilha/                           # Módulos 00 a 10 da trilha de estudos
├── BACKLOG.md                        # Pendências e estado atual (arquivo quente)
├── CLAUDE.md                         # Regras locais para agentes de IA
├── CONTEXT.md                        # Contexto estável do projeto para agentes
├── CONTRIBUTING.md                   # Como contribuir
├── FONTES.md                         # Fontes, autores, licenças e data de conferência
├── LICENSE                           # Licença MIT do texto original
├── README.md                         # Esta página
└── ROADMAP.md                        # Itens planejados
```

## Documentação de Apoio

- [Índice da documentação](docs/README.md)
- [Verificação de links](docs/verificacao-de-links.md)
- [Como contribuir](CONTRIBUTING.md)
- [Roadmap](ROADMAP.md)

## Contribuir

Sugestões de recursos, correções de link e resumos originais em português são bem-vindos. Leia [CONTRIBUTING.md](CONTRIBUTING.md) e o [ROADMAP.md](ROADMAP.md).

## Licença

O texto original deste repositório (organização, descrições e scripts) usa a licença [MIT](LICENSE). Os materiais linkados pertencem aos seus autores e seguem as licenças deles.
