# Backlog: trilha-ia

> Arquivo quente, atualizado ao fim de cada sessão (skill `backlog-e-memoria`).

## Próximo passo imediato
- Decidir se o verificador de links deve tratar 503 persistente do github.com como aviso (hoje ainda pode falhar o CI de vez em quando) e rodar o workflow `Verificar links` no GitHub para confirmar o comportamento real.

## Concluído recentemente
- 2026-11-23: repositório público criado e publicado (commit inicial com 22 arquivos).
- 2026-11-23: verificador de links com 2 conexões e retry em 429/5xx (de 32 falhas para 2, ambas falsas).
- 2026-11-23: repositório, pasta local e User-Agent renomeados para `trilha-ia`.
- 2026-11-23: `CONTEXT.md`, `BACKLOG.md` e `CLAUDE.md` adicionados.
- 2026-11-23: README adaptado ao padrão global de documentação e `docs/` criado (índice e manual de verificação de links).

## Pendências abertas
- O verificador leva cerca de 4 minutos; avaliar retry mais longo só para github.com e ritmo normal para os demais.
- Manuais em `docs/`: só existe `verificacao-de-links.md`. Novos manuais entram no índice (`docs/README.md`) e na barra de navegação.
- Notebooks e links não foram executados nem abertos um a um; a conferência foi só de status HTTP.

## Próximos passos candidatos
- Itens do `ROADMAP.md`: glossário, resumos originais por módulo, exercícios, mapa visual, leituras complementares, módulos novos (avaliação de LLMs, segurança e governança, IA em processos de negócios).
- Criar o rótulo `roadmap` no GitHub, citado no `ROADMAP.md`.
- Conferir de novo as fontes de `FONTES.md` (licenças e links) em data futura e atualizar a data de conferência.

## Notas para retomar rápido
- Pasta local: `~/Projetos/trilha-ia`. Remote: `origin` em https://github.com/jlazarete/trilha-ia.
- Falhas 503 em github.com na verificação são limite de requisições, não link quebrado. Retestar com `curl` antes de corrigir qualquer link.
- Tópicos do repositório: ia, inteligencia-artificial, machine-learning, llm, rag, agentes-de-ia, pt-br, trilha-de-estudos.
