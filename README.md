<div align="center">
  <h1>Navid API</h1>
  <p><strong>A Modernized, Ultra-Low Latency Stock API</strong></p>

  <p>
    <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI" />
    <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" alt="SQLAlchemy" />
    <img src="https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white" alt="Poetry" />
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  </p>
</div>

---

## ⚡ Core Philosophy

Navid is engineered with a singular focus: **Ultra-Low Latency** coupled with **Maximum Reliability**. Built on a high-performance modern Python stack, it provides a robust foundation for mission-critical financial applications.

## 🚀 The Possibilities

What can you build with Navid? The architecture empowers you to create:

- **Algorithmic Trading Engines:** Leverage real-time data flow with minimal overhead for high-frequency strategies.
- **Quantitative Research Platforms:** Feed massive datasets directly into your models seamlessly.
- **Real-Time Dashboards:** Power live stock tracking applications with absolute confidence in data integrity.
- **Automated Portfolio Management:** Execute rebalancing and trade triggers instantly.

## 🛠 Tech Stack

- **Framework:** FastAPI (Asynchronous, Type-safe)
- **ORM:** SQLAlchemy 2.0 (Dynamic models, Multiple database binds)
- **Environment:** Poetry (Deterministic dependency management)

## 🏁 Quickstart

Get up and running in seconds.

```bash
# Clone the repository
git clone https://github.com/your-username/navid.git
cd navid

# Install dependencies using Poetry
poetry install

# Start the high-performance server
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

> **Note:** Navid uses dynamic database querying and multiple binds (`stocks_dict`, `today_chart`). Ensure your database configuration is set up before starting the server.

---
<div align="center">
  <i>Engineered for speed. Built for scale.</i>
</div>
