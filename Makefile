help:
	@echo "Available targets:"
	@echo "  help             - Show this help message"
	@echo "  mkdocs-build     - Build web docs using mkdocs"
	@echo "  mkdocs-serve     - Serve web docs using mkdocs"
	@echo "  mkdocs-gh-deploy - Deploy web docs to GitHub Pages using mkdocs"
	@echo "  mddocs-build     - Build markdown docs using mddocs"

# --------------------------------------------------

MKDOCS_INSTALL = mkdocs-install.done

$(MKDOCS_INSTALL):
	pip install mkdocs mkdocs-material mkdocstrings[python] mkdocs-gen-files 
	touch $(MKDOCS_INSTALL)

MKDOCS_DIR = docs-web

$(MKDOCS_DIR):
	@if [ ! -d "$(MKDOCS_DIR)" ]; then mkdir -p "$(MKDOCS_DIR)"; fi

mkdocs-build: $(MKDOCS_INSTALL) $(MKDOCS_DIR)
	PYTHONPATH=./src mkdocs build

mkdocs-serve: $(MKDOCS_INSTALL) $(MKDOCS_DIR)
	PYTHONPATH=./src mkdocs serve

mkdocs-gh-deploy: $(MKDOCS_INSTALL) $(MKDOCS_DIR)
	PYTHONPATH=./src mkdocs gh-deploy

mkdocs-clean:
	rm -rf $(MKDOCS_DIR)
	rm -rf docs-web-site

# --------------------------------------------------

MDDOCS_INSTALL = mddocs-install.done

$(MDDOCS_INSTALL):
	pip install pydoc-markdown 
	touch $(MDDOCS_INSTALL)

MDDOCS_DIR = docs-md

$(MDDOCS_DIR):
	@if [ ! -d "$(MDDOCS_DIR)" ]; then mkdir -p "$(MDDOCS_DIR)"; fi

mddocs-bootstrap: $(MDDOCS_INSTALL) $(MDDOCS_DIR)
	pushd $(MDDOCS_DIR) && pydoc-markdown --bootstrap docusaurus && popd

PYUTILS := $(wildcard src/pyutils/*.py)

MDDOCS_GENERATE = mddocs_generate.done

$(MDDOCS_GENERATE): $(MDDOCS_INSTALL) $(MDDOCS_DIR) $(PYUTILS)
	pushd $(MDDOCS_DIR) && pydoc-markdown && popd 
	touch $(MDDOCS_GENERATE)

MDDOCS_INDEX_MD_TABLE = mddocs_index_md_table.done

$(MDDOCS_INDEX_MD_TABLE): $(MDDOCS_GENERATE)
	python scripts/mddocs/gen_index_md_table.py \
		--sidebar $(MDDOCS_DIR)/docs/reference/sidebar.json \
		--docs-root $(MDDOCS_DIR)/docs \
		--out $(MDDOCS_DIR)/docs/index.md

mddocs-build: \
	$(MDDOCS_GENERATE) \
	$(MDDOCS_INDEX_MD_TABLE)
