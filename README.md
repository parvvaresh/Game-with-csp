# Kakuro Game with CSP

[![Lint](https://github.com/OWNER/REPO/actions/workflows/lint.yml/badge.svg)](https://github.com/parvvaresh/Kakuro/actions/workflows/lint.yml)

[![Docker Test](https://github.com/OWNER/REPO/actions/workflows/docker-test.yml/badge.svg)](https://github.com/parvvaresh/Kakuro/actions/workflows/docker-test.yml)

This project is an implementation of the **Kakuro puzzle game** using **Constraint Satisfaction Problem (CSP)** techniques in Python.

## Project Structure
```

.
├── agent.py          # Main CSP agent logic
├── ai\_agent.py       # AI solver for Kakuro
├── game.py           # Game management and rules
├── main.py           # Entry point to run the game
├── cell\_set/         # Cell definitions and constraints
├── Dockerfile        # Containerization setup
└── README.md

````

## Run the Game
```bash
python main.py
````

## Run with Docker

```bash
docker build -t kakuro-game .
docker run --rm kakuro-game
```

