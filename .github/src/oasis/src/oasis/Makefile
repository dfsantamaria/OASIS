install:
	pip install -e .[dev]

test:
	pytest -v

lint:
	ruff check .
	black --check .

format:
	black .
Recommended Repo Structure
OASIS/
├── .github/
│   ├── workflows/
│   │   └── oasis-elite-ci.yml
│   └── dependabot.yml
├── src/oasis/
├── tests/
├── pyproject.toml
├── requirements.txt
├── README.md
├── Makefile
└── .gitignore
First Commands To Run
mkdir -p .github/workflows src/oasis tests
git add .
git commit -m "Initialize elite OASIS structure"
git push
