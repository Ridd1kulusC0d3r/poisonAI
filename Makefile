PY ?= python3
.PHONY: all checar site docs dose medir caso zumbis
all: checar medir site docs
checar:
	$(PY) scripts/construir.py --checar
site:
	$(PY) scripts/construir.py
docs:
	$(PY) scripts/gerar_docs.py
dose:
	$(PY) scripts/dose_resposta.py
# medição do portão em dados sintéticos (determinística, segundos)
medir:
	$(PY) scripts/medir_portao.py
# reconstrói o lote na lista oficial de CVEs (clone parcial, ~80 MB, alguns minutos)
caso:
	$(PY) scripts/caso_cve.py
# captura direta do estado dos registros rejeitados (precisa de internet)
zumbis:
	$(PY) scripts/zumbis.py
