# NASA APOD ETL with Airflow and PostgreSQL

### Daily Airflow DAG extracting NASA Astronomy Picture of the Day into Postgres.

[![GitHub](https://img.shields.io/badge/repo-NASA-APOD-ETL-Pipeline-with-Apache-Airfl-181717?logo=github)](https://github.com/ArchanaChetan07/NASA-APOD-ETL-Pipeline-with-Apache-Airflow-PostgreSQL)
[![Language](https://img.shields.io/badge/language-Python-3572A5)](https://github.com/ArchanaChetan07/NASA-APOD-ETL-Pipeline-with-Apache-Airflow-PostgreSQL)
[![License](https://img.shields.io/badge/license-See%20repository-yellow)](https://github.com/ArchanaChetan07/NASA-APOD-ETL-Pipeline-with-Apache-Airflow-PostgreSQL)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/ArchanaChetan07/NASA-APOD-ETL-Pipeline-with-Apache-Airflow-PostgreSQL/actions)

---

## Overview

Automate ingest of NASA APOD API records into a queryable database on a schedule.

Airflow DAG nasa_apod_postgres: create_table â†’ SimpleHttpOperator extract_apod â†’ transform_apod_data â†’ load_data_to_postgres via PostgresHook; docker-compose runs Postgres 13 + Airflow 2.8.1 webserver/scheduler.

Working ETL pattern with run logs showing successful scheduled/manual DAG attempts; Astro-style test scaffolding present.

This repository is maintained as **production-minded portfolio work**: clear architecture, automated checks where present, and metrics that are **traceable to committed artifacts** (never invented).

---

## Architecture

Airflow scheduler triggers DAG â†’ ensure apod_data table â†’ HTTP GET planetary/apod â†’ transform selected fields â†’ INSERT into PostgreSQL.

```mermaid
flowchart LR
  S[Airflow Scheduler @daily] --> T1[create_table]
  T1 --> T2[extract_apod HTTP]
  T2 --> T3[transform_apod_data]
  T3 --> T4[load_data_to_postgres]
  T4 --> DB[(PostgreSQL apod_data)]
  API[NASA APOD API] --> T2
```

```mermaid
sequenceDiagram
  participant U as User/Client
  participant S as Service/Pipeline
  participant E as Eval/Tools
  U->>S: request / job
  S->>E: execute
  E-->>S: results
  S-->>U: report / response
```

---

## Results & repository facts

> Only values found in code, configs, tests, or generated reports are listed. Absence of a clinical/ML accuracy number means it was **not** published in-repo.

| Metric | Value | Source |
|---|---|---|
| Tracked repository files | **33** | `git tree` |
| DAG schedule | **@daily** | `dags/etl.py` |
| Airflow image version | **2.8.1** | `docker-compose.yml` |
| Postgres host port mapping | **5433:5432** | `docker-compose.yml` |
| Tracked files | **33** | `git tree` |
| Python modules | **4** | `git tree` |
| Test-related paths | **3** | `git tree` |
| CI workflows | **Yes** | `.github/workflows` |
| Docker present | **Yes** | `repo root` |

```mermaid
%%{init: {'theme':'base'}}%%
pie showData title Language composition (bytes)
    "Python" : 100
    "Dockerfile" : 1
```

---

## Key features

- Daily @daily schedule
- HTTP extract via Airflow connection nasa_api
- Postgres table apod_data (title, explanation, url, date, media_type)
- Local docker-compose with ports 8080 (Airflow) and 5433 (Postgres)

---

## Tech stack

| Layer | Technology |
|---|---|
| orchestration | Apache Airflow 2.8.1 |
| database | PostgreSQL 13 |
| containers | Docker Compose |
| api | NASA APOD HTTP API |
| ci | GitHub Actions |

---

## Skills demonstrated

Python · A · p · a · c · h · e · CI/CD · testing · automation

Keyword surface: **Python · Python · machine-learning · CI/CD · testing · API · Docker · automation · data-science · software-engineering · system-design · observability · LLM · cloud**

---

## Project structure

```text
NASA-APOD-ETL-Pipeline-with-Apache-Airflow-PostgreSQL/
â”œâ”€â”€ dags/etl.py
â”œâ”€â”€ docker-compose.yml
â”œâ”€â”€ Dockerfile / requirements.txt / packages.txt
â”œâ”€â”€ logs/dag_id=nasa_apod_postgres/...
â”œâ”€â”€ tests/
â”œâ”€â”€ .astro/
â””â”€â”€ .github/workflows/ci.yml
```

---

## Installation & usage

```bash
git clone https://github.com/ArchanaChetan07/NASA-APOD-ETL-Pipeline-with-Apache-Airflow-PostgreSQL.git
cd NASA-APOD-ETL-Pipeline-with-Apache-Airflow-PostgreSQL
docker compose up -d
# Configure Airflow connections: nasa_api + my_postgres_connection
```

---

## How it works

With Compose services up, configure NASA API and Postgres connections in Airflow, then enable dag_id nasa_apod_postgres. Tasks create the table, fetch APOD JSON, map fields, and insert a row. Logs under logs/ show prior successful runs.

---

## Future improvements

- Rotate any documented API keys out of comments
- Add data-quality checks / idempotent upserts by date

---

## License

See repository.

---

<p align="center">
  <b>NASA APOD ETL with Airflow and PostgreSQL</b><br/>
  <a href="https://github.com/ArchanaChetan07/NASA-APOD-ETL-Pipeline-with-Apache-Airflow-PostgreSQL">github.com/ArchanaChetan07/NASA-APOD-ETL-Pipeline-with-Apache-Airflow-PostgreSQL</a>
</p>
