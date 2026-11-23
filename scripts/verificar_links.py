#!/usr/bin/env python3
"""Confere os links http(s) dos arquivos .md do repositório.

Uso: python3 scripts/verificar_links.py
Sai com código 1 se algum link falhar.
Alguns domínios bloqueiam robôs e são ignorados (ver IGNORAR).
"""
import re, sys, pathlib, urllib.request, urllib.error, urllib.parse
from concurrent.futures import ThreadPoolExecutor

RAIZ = pathlib.Path(__file__).resolve().parent.parent
IGNORAR = ("youtube.com", "youtu.be", "colab.research.google.com", "amazon.com", "aka.ms", "madewithml.com")
PADRAO = re.compile(r"\]\((https?://[^)\s]+)\)")

def coletar():
    urls = {}
    for arq in RAIZ.rglob("*.md"):
        for u in PADRAO.findall(arq.read_text(encoding="utf-8")):
            urls.setdefault(u, set()).add(str(arq.relative_to(RAIZ)))
    return urls

def checar(u):
    host = urllib.parse.urlparse(u).netloc
    if any(host.endswith(d) for d in IGNORAR):
        return u, "ignorado"
    req = urllib.request.Request(u, headers={"User-Agent": "trilha-ia-ptbr-link-check"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return u, r.status
    except urllib.error.HTTPError as e:
        return u, e.code
    except Exception as e:
        return u, f"erro: {e}"

def main():
    urls = coletar()
    with ThreadPoolExecutor(8) as ex:
        resultados = list(ex.map(checar, urls))
    falhas = [(u, s) for u, s in resultados if s != "ignorado" and not (isinstance(s, int) and s < 400)]
    for u, s in falhas:
        print(f"FALHOU [{s}] {u} em {sorted(urls[u])}")
    print(f"{len(urls)} links, {len(falhas)} falhas")
    return 1 if falhas else 0

if __name__ == "__main__":
    sys.exit(main())
