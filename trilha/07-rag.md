# Módulo 7: RAG: recuperação e geração aumentada

**Objetivo:** Começar pelo RAG simples e ir adicionando técnicas de consulta, chunking, recuperação, avaliação e arquiteturas avançadas.

## Antes de começar

- Módulo 6, principalmente o capítulo de busca semântica.
- A ordem das categorias segue a organização do README do RAG_Techniques.

**Fontes deste módulo:** [Hands-On Large Language Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models) (Jay Alammar e Maarten Grootendorst, Apache 2.0), [RAG Techniques](https://github.com/NirDiamant/RAG_Techniques) (Nir Diamant, Licença própria, uso não comercial com atribuição).

## Passo a passo

Marque cada item ao concluir (use uma cópia do repositório com fork para manter seu progresso).

- [ ] **7.0. Base conceitual**: capítulo 8 do livro Hands-On LLM, "Busca semântica e RAG": [pasta do capítulo](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models/tree/main/chapter08).


### Fundamentos de RAG

- [ ] **7.1. RAG simples**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/simple_rag.ipynb).
- [ ] **7.2. RAG simples com CSV**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/simple_csv_rag.ipynb).
- [ ] **7.3. RAG confiável**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/reliable_rag.ipynb).
- [ ] **7.4. Escolha do tamanho de chunk**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/choose_chunk_size.ipynb).
- [ ] **7.5. Chunking por proposições**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/proposition_chunking.ipynb).
- [ ] **7.6. RAG simples com JSON**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/json_rag.ipynb).
- [ ] **7.7. RAG local com Hugging Face e FAISS**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/local_rag_huggingface_faiss.ipynb).
- [ ] **7.8. Parsing de documentos com OCR**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/document_parsing_with_mistral_ocr.ipynb).

### Melhoria da consulta

- [ ] **7.9. Transformações da consulta**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/query_transformations.ipynb).
- [ ] **7.10. HyDE (documento hipotético)**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/HyDe_Hypothetical_Document_Embedding.ipynb).

### Enriquecimento de contexto e conteúdo

- [ ] **7.11. HyPE (embeddings de prompts hipotéticos)**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/HyPE_Hypothetical_Prompt_Embeddings.ipynb).
- [ ] **7.12. Cabeçalhos contextuais de chunk**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/contextual_chunk_headers.ipynb).
- [ ] **7.13. Extração de segmento relevante**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/relevant_segment_extraction.ipynb).
- [ ] **7.14. Enriquecimento com janela em torno do chunk**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/context_enrichment_window_around_chunk.ipynb).
- [ ] **7.15. Chunking semântico**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/semantic_chunking.ipynb).
- [ ] **7.16. Compressão contextual**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/contextual_compression.ipynb).
- [ ] **7.17. Aumento de documentos por geração de perguntas**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/document_augmentation.ipynb).

### Recuperação avançada

- [ ] **7.18. Fusion retrieval**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/fusion_retrieval.ipynb).
- [ ] **7.19. Reranking**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/reranking.ipynb).
- [ ] **7.20. Filtragem multifacetada**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/multi_faceted_filtering.ipynb).
- [ ] **7.21. Índices hierárquicos**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/hierarchical_indices.ipynb).
- [ ] **7.22. Dartboard retrieval**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/dartboard.ipynb).
- [ ] **7.23. RAG multimodal com legendas**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/multi_model_rag_with_captioning.ipynb).
- [ ] **7.24. RAG multimodal com ColPali**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/multi_model_rag_with_colpali.ipynb).

### Técnicas iterativas e adaptativas

- [ ] **7.25. Recuperação com ciclo de feedback**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/retrieval_with_feedback_loop.ipynb).
- [ ] **7.26. Recuperação adaptativa**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/adaptive_retrieval.ipynb).

### Avaliação

- [ ] **7.27. Métricas de avaliação**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/evaluation/define_evaluation_metrics.ipynb).
- [ ] **7.28. Avaliação com DeepEval**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/evaluation/evaluation_deep_eval.ipynb).
- [ ] **7.29. Avaliação com GroUSE**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/evaluation/evaluation_grouse.ipynb).
- [ ] **7.30. Avaliação ponta a ponta de RAG**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/evaluation/end-2-end_rag_evaluation.ipynb).
- [ ] **7.31. Open-RAG-Eval**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/evaluation/open-rag-eval-example.ipynb).

### Memória e explicabilidade

- [ ] **7.32. MemoRAG**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/memorag.ipynb).
- [ ] **7.33. Recuperação explicável**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/explainable_retrieval.ipynb).

### Arquiteturas avançadas

- [ ] **7.34. RAG agêntico**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/Agentic_RAG.ipynb).
- [ ] **7.35. Graph RAG**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/graph_rag.ipynb).
- [ ] **7.36. Graph RAG com Milvus**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/graphrag_with_milvus_vectordb.ipynb).
- [ ] **7.37. GraphRAG da Microsoft**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/Microsoft_GraphRag.ipynb).
- [ ] **7.38. RAPTOR**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/raptor.ipynb).
- [ ] **7.39. Self-RAG**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/self_rag.ipynb).
- [ ] **7.40. RAG corretivo (CRAG)**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/crag.ipynb).
- [ ] **7.41. Graph RAG local com atribuição verificável**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/graph_rag_local_attribution.ipynb).
- [ ] **7.42. LightRAG**: [notebook no GitHub (inglês)](https://github.com/NirDiamant/RAG_Techniques/blob/main/all_rag_techniques/light_rag.ipynb).

## Observações

- ATENÇÃO À LICENÇA: o RAG_Techniques usa uma licença própria que permite uso não comercial com atribuição e reserva os direitos comerciais ao autor. Por isso este repositório só aponta links para ele e não copia nenhum arquivo. Se for usar o código dele em trabalho comercial, leia a [licença](https://github.com/NirDiamant/RAG_Techniques/blob/main/LICENSE) e peça autorização ao autor.
- O README do RAG_Techniques indica que a técnica de número 37 (agente controlável para tarefas complexas de RAG) fica em outro repositório do autor: [Controllable-RAG-Agent](https://github.com/NirDiamant/Controllable-RAG-Agent).
- Existem também versões com LlamaIndex de alguns notebooks (por exemplo RAG simples, fusion retrieval e reranking) na mesma pasta.

---
[← Módulo anterior](06-llms-na-pratica.md) | [Próximo módulo →](08-agentes-de-ia.md)
