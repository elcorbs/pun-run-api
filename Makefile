.PHONY: activate
activate:
	( \
           source /pun-run/bin/activate; \
           pip install -r requirements.txt; \
	)
