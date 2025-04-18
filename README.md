# NASA APOD ETL Pipeline with Apache Airflow and PostgreSQL

This project builds an **ETL pipeline using Apache Airflow** that fetches NASA's Astronomy Picture of the Day (APOD) using their public API, processes the data, and stores it in a **PostgreSQL** database.

---

## 🚀 What the Pipeline Does

The DAG `nasa_apod_postgres` performs the following tasks daily:

1. **Create Table**: Creates `apod_data` table in PostgreSQL if not exists.
2. **Extract APOD**: Calls NASA's APOD API to fetch daily astronomical image and metadata.
3. **Transform**: Extracts necessary fields from JSON.
4. **Load**: Inserts the data into PostgreSQL.

---

## 🔧 Technologies Used

- [Apache Airflow 2.8.1](https://airflow.apache.org/) with LocalExecutor
- [PostgreSQL 13](https://www.postgresql.org/)
- [Docker + Docker Compose](https://docs.docker.com/compose/)
- [NASA APOD API](https://api.nasa.gov/)

---

## 🧪 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/ArchanaChetan07/NASA-APOD-ETL-with-Apache-Airflow-PostgreSQL.git
cd NASA-APOD-ETL-with-Apache-Airflow-PostgreSQL
```

### 2. Add NASA API Key

Edit your `.env` or create a new Airflow connection in the UI:

- Visit: http://localhost:8080
- Navigate: **Admin > Connections > Create**
- Conn Id: `nasa_api`
- Conn Type: `HTTP`
- Host: `https://api.nasa.gov`
- Extras:
```json
{
  "api_key": "YOUR_API_KEY_HERE"
}
```

> 🔑 Get your free API key from: [https://api.nasa.gov](https://api.nasa.gov)

### 3. Start Airflow & PostgreSQL using Docker Compose

```bash
docker-compose up -d --build
```

Wait for all containers to be healthy (`webserver`, `scheduler`, `postgres_db`).

### 4. Initialize Airflow and Create Admin User

```bash
docker-compose run airflow-init
```

This will create:
- Admin user: `admin` / `admin`
- All DB tables and metadata

### 5. Access Airflow UI

Go to: [http://localhost:8080](http://localhost:8080)  
Login with:
```
Username: admin
Password: admin
```

### 6. Enable and Trigger the DAG

- Search for `nasa_apod_postgres`
- Turn it **ON**
- Click ▶️ to trigger the DAG manually

---

## 📊 PostgreSQL Output Table

The `apod_data` table contains:

| id | title | explanation | url | date | media_type |
|----|-------|-------------|-----|------|-------------|
| 1  | Image Title | Description | Image URL | YYYY-MM-DD | image / video |

You can view it with [DBeaver](https://dbeaver.io/) or `psql` command line.

---

## Troubleshooting

- PostgreSQL port conflicts? Change `5432:5432` to `5433:5432` in `docker-compose.yml`
- Airflow webserver not reachable? Wait a minute after starting or restart the container.
- API errors? Make sure your key is valid and you haven’t exceeded NASA rate limits.

