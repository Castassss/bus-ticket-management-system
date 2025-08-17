# Project — Bus Ticket Management System (Python + PostgreSQL)

Console application in **Python + PostgreSQL** with two profiles:
- **Customer**: register/login, view destinations/trips, buy tickets (with waiting list), view messages, cancel tickets, **Gold plan** (10% discount).
- **Administrator**: manage buses, create/remove trips, change prices (with history), send messages to customers, sales statistics.

> Main code: `Projeto.py` (global menu) and `Cliente.py` (customer functions).  
> Database: PostgreSQL (tables such as `cliente`, `viagem`, `bilhete`, `autocarros`, `tipo_viagem`, `mensagem_cliente`, …).

---

## Requirements
- Python 3.10+
- PostgreSQL 13+ (with a DB named **`Projeto`**)
- Python dependencies: `psycopg2-binary`

Install dependencies:
```bash
pip install -r requirements.txt
```

## Database
1) Create the database (in psql):
```sql
CREATE DATABASE "Projeto";
```
2) Create the tables (minimum functional — adjust if necessary):
```sql
\c "Projeto"
-- execute the content of schema.sql
```

> **Current credentials** (hard-coded in code): host `localhost`, user `postgres`, password `postgres`.  
> It is recommended to move these to environment variables/.env and use `python-dotenv`.

## How to Run
```bash
# 1) (optional) virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2) install deps
pip install -r requirements.txt

# 3) PostgreSQL running and DB ready (see "Database" section)

# 4) start application (global menu)
python "Projeto/Projeto.py"
```
Initial menu:
- **1) Customer** → `Cliente.escreve_cliente()`
- **2) Administrator** → `escreve_administrador()`
- **3) Exit`

## Features (summary)
- **Customer**
  - Register and authenticate.
  - View **destinations** and **available trips**.
  - **Buy tickets** (decreases capacity; if 0 → goes to **waiting list**).
  - **Gold Plan**: **10% discount** on shown price.
  - View **messages** from administrator (marked as seen).
  - View and **cancel** tickets.
- **Administrator**
  - **Buses**: add, list, update number of seats.
  - **Trips**: create (linked to `tipo_viagem` and `autocarros`), change price (stored in `historico`), remove.
  - **Messages to customers**: created in `mensagem_cliente` and linked in `cliente_mensagem_cliente`.
  - **Statistics**: day/month with most sales (aggregations by `data_partida`/`bilhete`).

## Improvements Needed
- **SQL injection:** there are `cur.execute("... %d" % var)` which must be replaced by **placeholders** and tuples: `cur.execute("... WHERE id=%s", (var,))`.
- **Passwords in plain text:** apply hashing (e.g.: `bcrypt`) and `psycopg2.sql`/parameterization.
- **Portability:** `os.system('cls')` is Windows-only; use `cls`/`clear` depending on `os.name`.
- **Config separation:** move credentials to `.env` and read with `os.getenv`.
- **Code structure:** add `if __name__ == "__main__":` and separate UI/DB logic into modules.

## Current Structure
```
Projeto/
├── Cliente.py
├── Projeto.py
├── Diagrama Entidade.json
├── Diagrama_Antigo.png
├── Diagrama_Físico_Antigo.png
├── Diagrama_Fisico_Novo.png
├── Novo_Diagrama.png

```

## Report
The final report can be accessed at the following link (Dropbox):  
[Projeto-BD.pdf](https://www.dropbox.com/scl/fi/eq2f968a1c18jikamrq6k/Projeto-BD.pdf?rlkey=5vna66dfjqng55rd1hfk3xnv1&st=0gaejbo7&dl=0)

Access is restricted → please request access if needed.

```

## License
No explicit license included. Consider adding one (e.g., MIT).
