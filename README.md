## GovTech DSAID AI Bots 🤖

### Youtube Demo

To watch the full-stack application in action do checkout the video in this [Link](https://youtu.be/8bYJQtIn5ow)

### Tech Stack 🥞

The repository is a full-stack web application for interaction with OpenAI's LLM, the following is the tech-stack used:

- MongoDB 🍃
- Docker 🐳
- Python FastAPI 🚀
- NextJS ⏭️

---

### Running Locally 🏃🏻‍♀️

Before running the application locally, ensure that you `docker` installed, and `.env` in the **root** directory of the project. The `.env` file should contain the following keys:

```
OPENAI_API_KEY=...
MONGODB_ROUTE=...
ENCRYPTION_KEY=...
NEXT_PUBLIC_API_ENDPOINT=...
```

Once the `.env` file is in root, we can run the following docker compose command to start our application:

```
docker compose up
```

Once the images have been pulled, and containers provisioned we will have 4 containers running with the names and port of:

- **mongodb** | `27017`
- **mongo-express** |`8081
- **frontend** |`3000`
- **backend** |`8000`

---

### Testing Locally 🧪

#### Testing APIs w/ pytest 🐍

To test APIs for **Test Driven Development (TDD)**, run the following commands:

```
docker compose up -d
cd ./backend
pip install -r requirements.txt
cd ./tests
pytest test_apis.py
```

#### Postman 📩

In the repository, a json configuration file named `ESD Project.postman_collection.json` is provided. To test the API suite import the json file into Postman using the following steps:

- On the top left corner click _Import_
- Click _Choose Files_ and navigate to where the configuration file is or drag & drop
  Test the APIs like you normally would with Postman

#### Mongo-Express 🍀

To test adding and deletion of documents, navigate to `http://localhost:8081` and use Mongo-Express. Mongo-Express allows you to view databases, collections and documents in your database.

#### Frontend & Backend ⌨️

## If you wish to test frontend & backend without the need for Docker, navigate to `./frontend` and `./backend` for individual instructions.
