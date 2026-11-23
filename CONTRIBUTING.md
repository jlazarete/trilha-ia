# Como contribuir

Obrigado por querer melhorar a trilha. O objetivo é ter um guia de estudo confiável em português, então a regra central é: **nada de cópia e nada de invenção**.

## O que aceitamos

- Correção de link quebrado ou de título.
- Sugestão de novo recurso aberto para um módulo existente.
- Resumos, glossários e exercícios **originais** em português, com fontes citadas.
- Relato de item que parou de funcionar (versão de biblioteca, API que mudou).

## O que não aceitamos

- Cópia de trechos, imagens, notebooks ou traduções integrais de material de terceiros.
- Recursos sem licença clara ou pagos sem aviso.
- Afirmações sobre o conteúdo que você não verificou na fonte.

## Critérios para sugerir um recurso

1. Está aberto e acessível sem pagamento (ou o custo está explícito).
2. Tem autor e licença identificáveis.
3. Tem uma ordem de estudo clara ou se encaixa em um módulo.
4. Você consegue indicar o que ele ensina com base no próprio material.

## Fluxo

1. Abra uma issue usando o modelo adequado.
2. Para mudar arquivos, faça um fork, crie uma branch (`feat/...`, `fix/...`, `docs/...`) e abra um pull request.
3. Rode a verificação de links antes de enviar:

   ```bash
   python3 scripts/verificar_links.py
   ```

4. Use mensagens de commit no padrão Conventional Commits, por exemplo `fix(modulo-07): corrige link do notebook de reranking`.

## Estilo de escrita

- Português do Brasil, direto e claro.
- Sem travessões longos.
- Itens de estudo em lista com caixa de seleção (`- [ ]`), com link para a fonte e indicação de idioma.

## Conduta

Seja respeitoso. Críticas são sobre o conteúdo, não sobre as pessoas.
