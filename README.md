📘 README.md — Pyton Package Using Conda

A fully self‑healing, auto-fixing, auto‑versioned, auto‑releasing MLOps system.

 

🚀 Overview

OASIS is a fully autonomous Machine Learning + DevOps hybrid pipeline featuring:

Real‑dataset LightGBM training

Versioned model saving

Semantic versioning

Full CLI toolkit ( oasis train ,  oasis version ,  oasis auto‑fix , etc.)

Automatic changelog generation

Automatic GitHub Releases

CI Retry + Auto‑Merge system

PR‑based self‑healing

Auto‑close failing PRs

Nightly auto‑fix pipelines

Auto‑formatting, linting, diagnostics, and repository cleanup

OASIS maintains itself — heals its own repo, fixes CI failures, formats code, retries CI, publishes releases, updates changelogs, and more.

 

📁 Project Structure

 
OASIS/
│
├── data/
│   └── dataset.csv
│
├── models/
│   ├── trained_model.pkl
│   ├── version.txt
│   └── history.log
│
├── src/
│   ├── train_pipeline.py
│   ├── model_loader.py
│   └── oasis/
│       └── cli.py
│
├── tests/
│   └── test_lgb_model.py
│
└── .github/workflows/
    ├── ci.yml
    ├── oasis-auto-fix.yml
    ├── oasis-auto-fix-pr.yml
    ├── oasis-auto-fix-nightly.yml
    ├── oasis-auto-merge.yml
    ├── oasis-auto-close.yml
    └── oasis-ci-retry.yml
 

 

🧠 Training Pipeline

Training uses:

 
src/train_pipeline.py
 

Pipeline includes:

Loading real dataset

Splitting training/test

Training LightGBM

Saving model + metadata

Recording semantic version

Appending version history

Train manually:

 
oasis train
 

 

🧪 Testing

Tests validate:

Model load

Feature alignment

Prediction behavior

Deterministic output

Run manually:

 
pytest -v
 

 

⚙️ GitHub Actions Overview

OASIS includes 7 fully autonomous workflows:

✔  ci.yml 

Standard train + test workflow.

✔  oasis-auto-fix.yml 

Self-heals repository on command.

✔  oasis-auto-fix-pr.yml 

Creates auto-fix PRs instead of pushing changes.

✔  oasis-auto-fix-nightly.yml 

Runs nightly repository healing at 2AM UTC.

✔  oasis-auto-merge.yml 

Auto-merges approved auto-fix PRs only when CI is green.

✔  oasis-auto-close.yml 

Auto-closes persistent failing PRs after 3 CI failures.

✔  oasis-ci-retry.yml 

Retries CI up to 3 times before merging or closing.

Combined, these workflows create a self-maintaining MLOps ecosystem.

 

🧵 OASIS CLI Commands

Your CLI includes:

🔧 Training & Model Management

 
oasis train
oasis evaluate <dataset.csv>
oasis predict <input.csv>
 

🔍 Model Metadata

 
oasis version
oasis version --json
 

Metadata includes:

Semantic version

Timestamp

Feature list

Model size

File path

🧾 Version History & Releases

 
oasis bump-version --level patch|minor|major
oasis history
oasis changelog
oasis release
 

Release automatically:

Tags Git

Generates changelog

Uploads model to GitHub Releases

🛠 Auto‑Fix & Formatting

 
oasis auto-fix
oasis auto-fix-strict
oasis format
oasis clean
 

🩺 Diagnostics

 
oasis doctor
oasis doctor --json
oasis doctor --fix
oasis doctor --fix --commit --push
 

Doctor checks:

Python syntax

YAML health

GPU availability

Missing dependencies

Model file integrity

Git status

Auto-healing

 

🤖 Self‑Healing DevOps Explained

OASIS includes autonomous maintenance loops:

1️⃣ Failure → Auto-Fix PR

A CI failure triggers a repair branch & PR.

2️⃣ Auto‑Retry CI

OASIS retries CI up to 3 times.

3️⃣ Auto‑Comment Failure Reasons

Explains why CI failed directly on PR.

4️⃣ Auto‑Merge

If CI passes + PR is approved → merge.

5️⃣ Auto‑Close

If CI fails 3 times → PR closed with explanation.

6️⃣ Nightly Repair

Nightly self-healing runs regardless of CI.

 

🚀 Release Automation

Release with:

 
oasis release
 

This:

Reads semantic version

Creates Git tag

Generates changelog

Uploads model

Publishes GitHub Release

Optional:

 
oasis release --no-confirm
oasis release --notes "Custom message"
 

 

🧹 Cleanup & Formatting

Run:

 
oasis clean
oasis format
 

Removes:

Caches

Build files

Logs

Model artifacts (optional)

And formats code using:

Black

isort

docformatter

 

📦 Installation

Editable mode installation:

 
pip install -e .
 

 

🛟 Support

If you need enhancements, improvements, or more automation, extend the CLI or GitHub workflows.

 

🎉 Final Note

This README documents your complete autonomous ML + DevOps pipeline.
Your OASIS system is now capable of:

Training

Testing

Healing

Formatting

Releasing

Versioning

Closing

Commenting

Auto-merging

Nightly cleaning

all without human intervention.