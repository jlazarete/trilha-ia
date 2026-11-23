# Verificação de links

---

<p align="center">
  <a href="README.md">Índice</a> • <strong>Verificação de links</strong>
</p>

---

O script [`scripts/verificar_links.py`](../scripts/verificar_links.py) confere todos os links `http(s)` escritos no formato Markdown `[texto](url)` nos arquivos `.md` do repositório. Ele usa só a biblioteca padrão do Python.

## Como rodar

```bash
python3 -I scripts/verificar_links.py
```

O código de saída é `0` quando tudo passa e `1` quando algum link falha. Cada falha aparece com o status e o arquivo de origem, e a última linha traz o total de links e de falhas.

> [!NOTE]
> A execução leva alguns minutos. O ritmo é lento de propósito, para não ser barrado pelo GitHub.

## Como funciona

- **Paralelismo:** 2 conexões simultâneas (`TRABALHADORES`).
- **Tentativas:** até 4 por link (`TENTATIVAS`) para erros transitórios: 429, 500, 502, 503, 504 e falhas de rede.
- **Espera entre tentativas:** 2, 4 e 8 segundos, ou o valor do cabeçalho `Retry-After` quando o servidor informa, limitado a 60 segundos.
- **Sem nova tentativa:** erros definitivos, como 404, falham de imediato.
- **Domínios ignorados:** `youtube.com`, `youtu.be`, `colab.research.google.com`, `amazon.com`, `aka.ms` e `madewithml.com`, porque bloqueiam robôs. A lista fica em `IGNORAR`, no script.

## Falha com 503 em github.com

> [!IMPORTANT]
> Um 503 em páginas do github.com costuma ser limite de requisições, não link quebrado. Antes de corrigir qualquer link, teste a URL sozinha:
>
> ```bash
> curl -s -o /dev/null -w "%{http_code}\n" -A trilha-ia-link-check "<url>"
> ```

Se a resposta for 200, o link está certo e a falha foi passageira. Rode o script de novo mais tarde. Se for 404, corrija o link no módulo indicado.

## Execução automática

O workflow [`links.yml`](../.github/workflows/links.yml) roda o mesmo script em pull requests, toda segunda-feira às 12h UTC e sob demanda (`workflow_dispatch`).
