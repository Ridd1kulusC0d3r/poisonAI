PY ?= python3
.PHONY: all checar site docs dose
all: checar site docs
checar:
	$(PY) scripts/construir.py --checar
site:
	$(PY) scripts/construir.py
docs:
	$(PY) scripts/gerar_docs.py
dose:
	$(PY) scripts/dose_resposta.py
