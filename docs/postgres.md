# Postgresql guide

## Create user and database

Let's assume we have docker container running Postgres on port 5435, and we want to create a user and a database for our Django application.

**Step 1: Connect to the Postgres container**

```bash
docker exec -it <container_name> psql -U postgres
```

Or,

```bash
docker exec -it <container_name> bin/bash
psql -U postgres
```

**Step 2: Create user and database**

Assuming you want to create a user named `myuser` with password `mypassword`, and a database named `boilerplate` owned by `myuser`, you can run the following SQL commands:

```sql
-- Create user
CREATE USER myuser WITH PASSWORD 'mypassword';

-- Create database and assign ownership to the user
CREATE DATABASE boilerplate OWNER myuser;

-- Connect to the new database
\c boilerplate

-- Ensure the user has full privileges on schema and all future objects
GRANT ALL PRIVILEGES ON DATABASE boilerplate TO myuser;
GRANT ALL ON SCHEMA public TO myuser;
ALTER SCHEMA public OWNER TO myuser;

-- Default privileges (future tables/functions/etc.)
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON FUNCTIONS TO myuser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TYPES TO myuser;
```
