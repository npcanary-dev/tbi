ROOT_DIR ?= .
SOURCE_DIR ?= $(ROOT_DIR)/src
BUILD_DIR ?= $(ROOT_DIR)/build
PROJECT_FILE ?= $(ROOT_DIR)/pyproject.toml
DCOMPOSE_FILE ?= $(ROOT_DIR)/docker-compose.yaml

DCOMPOSE ?= docker compose
PYC ?= python -m build
PIP ?= python -m pip
STC ?= python -m pyright
FMT ?= python -m black --config $(PROJECT_FILE)
IFMT ?= python -m isort

IGNORE_ERROR = 2>/dev/null || true

.PHONY: clean check wheel sdist

install :
	$(PIP) install $(ROOT_DIR) --force-reinstall --no-deps --no-cache-dir

full-install :
	$(PIP) install $(ROOT_DIR) --force-reinstall --no-cache-dir

wheel : | $(BUILD_DIR)
	$(PYC) --outdir $(BUILD_DIR) --wheel $(ROOT_DIR)

sdist : | $(BUILD_DIR)
	$(PYC) --outdir $(BUILD_DIR) --sdist $(ROOT_DIR)

docker-image :
	$(DCOMPOSE) -f $(DCOMPOSE_FILE) build

check :
	$(STC) -p $(PROJECT_FILE)

autoformat :
	$(FMT) $(SOURCE_DIR)
	$(IFMT) $(SOURCE_DIR)

$(BUILD_DIR) :
	mkdir -p $(BUILD_DIR)

clean :
	rm -r $(BUILD_DIR) $(IGNORE_ERROR)
	rm -r $(SOURCE_DIR)/*.egg-info $(IGNORE_ERROR)
