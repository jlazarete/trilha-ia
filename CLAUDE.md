# trilha-ia

Leia antes de qualquer tarefa:
@CONTEXT.md
@BACKLOG.md

## Regras deste projeto
- Responder em português do Brasil, direto, em checklist quando houver passos
- Tarefa com mais de um passo: aplicar a skill `orquestrador-agentes` (Haiku busca, Sonnet executa, Opus revisa)
- Lista de 3 ou mais tarefas: skill `tarefas-em-lote`, registrando no `TASKS.md`
- Conferir cada item do plano contra o diff antes de dizer que terminou
- Nunca rodar `git add`, `git commit` ou `git push` sem pedido explícito
- Nunca ler nem imprimir o conteúdo do `.env`
- Comandos Linux com `-v` quando a opção existir
- Texto para cliente ou público: skill `linguagem-cliente-lazarete` antes de entregar
- Ao encerrar a sessão: skill `backlog-e-memoria`

## Regras específicas da trilha
- Nada de cópia e nada de invenção: só links e descrições originais, sempre conferidas na fonte
- Todo recurso novo precisa de autor e licença identificáveis, acesso sem pagamento (ou custo explícito) e indicação de idioma
- Mudou link ou módulo: rodar `python3 -I scripts/verificar_links.py` e retestar com `curl` o que falhar com 503 antes de corrigir
- Mudou fonte, licença ou data de conferência: atualizar o `FONTES.md`
- Repositório público: nunca colocar e-mail, caminhos absolutos da máquina, tokens ou dados de clientes em nenhum arquivo
