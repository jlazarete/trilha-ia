# Contexto do projeto: trilha-ia

> Arquivo frio, lido por qualquer agente (Claude Code, Antigravity/Gemini) antes de começar.
> Muda pouco. O estado do dia a dia mora só no `BACKLOG.md`.

## 1. O que é o projeto
- Finalidade: trilha de estudos de IA em português, em ordem, do básico a agentes e produção, montada a partir de cursos abertos de referência.
- Resultado esperado: um guia confiável, com links verificados, idioma indicado e crédito a cada autor.
- Natureza: curadoria e ordenação. Não copia nem reescreve o conteúdo dos autores, só linka.
- Stack principal: Markdown, um script Python sem dependências externas (`scripts/verificar_links.py`) e GitHub Actions.
- Repositório: https://github.com/jlazarete/trilha-ia (público, licença MIT para o texto original).
- Estrutura: `trilha/00` a `trilha/10` (módulos), `FONTES.md` (fontes, licenças, data de conferência), `ROADMAP.md`, `CONTRIBUTING.md`, `.github/` (modelos e workflow de links).
- Proposta de origem: não há.

## 2. Estado atual
- Última atualização: `2026-11-23` por `Claude Code`
- Pulso de uma linha: versão 0.1 publicada, com 10 módulos e verificador de links com retry. Detalhes no `BACKLOG.md`.

## 3. Decisões já tomadas (log, não reabrir sem motivo)
- 2026-11-23: repositório criado a partir de um zip de curadoria e publicado como público.
- 2026-11-23: repositório renomeado de `trilha-ia-ptbr` para `trilha-ia`; pasta local e User-Agent do verificador renomeados junto.
- 2026-11-23: verificador de links usa 2 conexões em paralelo e até 4 tentativas para 429 e 5xx, porque o GitHub devolvia 503 em rajadas (32 falsos positivos com 8 conexões).
- 2026-11-23: youtube.com, youtu.be, Colab, Amazon, aka.ms e madewithml.com ficam fora da verificação (bloqueiam robôs).
- Princípios do README: sem cópia de material de terceiros, sem invenção de conteúdo, crédito e licença de cada fonte em `FONTES.md`.

## 4. Convenções do projeto
- Branches: `feat/...`, `fix/...`, `docs/...` (ver `CONTRIBUTING.md`). Commits só quando o José pedir; os dois primeiros foram direto na `main` a pedido dele.
- Commits: Conventional Commits, sem linha de coautoria nem trailer de IA.
- Segredos: só no `.env` (fora do git). O projeto não usa nenhum hoje.
- Texto em português do Brasil, direto, sem travessões longos.
- Itens de estudo em lista com caixa de seleção (`- [ ]`), com link para a fonte e indicação de idioma.
- Verificar links com `python3 -I scripts/verificar_links.py`. A execução leva alguns minutos por causa do retry.
- O que NUNCA fazer aqui:
  - copiar trechos, imagens, notebooks ou traduções integrais de material de terceiros;
  - afirmar o que um recurso ensina sem ter conferido na fonte;
  - indicar recurso sem licença clara ou pago sem avisar;
  - ocultar a licença de uso não comercial do RAG_Techniques no módulo 7.

## 5. Notas por ferramenta
### Claude Code
- Modelo: `opusplan` (Opus planeja no plan mode, Sonnet executa)
- Subagents usados: nenhum até agora.
- Skills relevantes: orquestrador-agentes, tarefas-em-lote, backlog-e-memoria, commits-git-lazarete, linguagem-cliente-lazarete

### Antigravity / Gemini
- Modelo usado:
- Limitações encontradas:

## 6. Handoff
Antes de encerrar a sessão: skill `backlog-e-memoria`, e só toque neste arquivo se algo frio mudou.
