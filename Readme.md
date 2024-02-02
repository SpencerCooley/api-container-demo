# Setup

if you are setting this up you need to place a .env file in the app/ directory. this file will contain all the environment variables needed to run the application. The following is a list of variable currently in use.

| Variable     | Description                                    |
| ------------ | ---------------------------------------------- |
| DATABASE_URL | URL for connecting to the application database |

# Database and connections

This application uses postgresql with sqlalchemy. The database is version controlled using alembic migrations. Any time you are changing the data models you need to generate migrations for your change and then commit them. This ensures we keep an orderly way of changing the database structure.

to generate a migration:
alembic revision --autogenerate -m "a message about model/database changes"

to commit your new changes:

```bash
alembic upgrade head
```

or (if you are rolling back to something):

```bash
alembic upgrade {version-hash}
```

# Docker related info

To enter an interactive terminal, follow these steps:

1. Look up the Docker process using the `docker ps` command:

   ```bash
   docker ps
   ```

2. Identify the desired Docker container in the list.

3. Enter the interactive terminal for the chosen container using the following command, replacing `{process_id}` with the actual process ID obtained from the `docker ps` command:

   ```bash
   docker exec -it {process_id} bash
   ```

If you make changes to the dockerfile of any configuration involving the build of the image then you need to rebuild the docker image with the following command.

```bash
docker build -t demo-fastapi .
```

To run the image in development mode with live code reloading then you just have to run

```bash
sh start-dev.sh
```

you can view application at http://localhost:8000
