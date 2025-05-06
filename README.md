# 🚀 Football NLU API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.68.0+-blue.svg)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-20.10.8+-blue.svg)](https://www.docker.com/)

A Natural Language Understanding API for football queries that combines intent detection and entity recognition to process natural language queries about football teams, matches, and results.

## 🔍 Project Overview

Football NLU API is a FastAPI-based service that understands natural language queries about football teams and matches. It leverages machine learning models to detect user intent and recognize football team entities, providing structured data responses that can be integrated into chat applications, voice assistants, or any football-related service.

### Key Features:
- 🧠 Natural Language Understanding for football queries
- 🏆 Team name entity recognition with fuzzy matching
- ⚽ Intent classification for match time, results, and team queries
- 📊 Upcoming and previous match information retrieval
- 🐳 Containerized with Docker for easy deployment

### Technology Stack:
- 🐍 Python 3.9
- 🚀 FastAPI web framework
- 🤖 SetFit for intent detection
- 🏷️ GLiNER for entity recognition
- 🔄 RapidAPI Football API integration
- 🐳 Docker for containerization

## 📥 Installation Guide

### Prerequisites:
- Python 3.9+
- Docker (optional for containerized deployment)
- Hugging Face API token (for accessing models)
- RapidAPI key for football data

### Local Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/football-nlu-api.git
   cd football-nlu-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requermint.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the project root with the following:
   ```
   hf_token = "your-huggingface-token"
   football_api = "your-rapidapi-football-api-key"
   setfit_model_id = "Ah7med/setfit-football_bootpress_paraph-multi-v2"
   gliner_model_id = "urchade/gliner_multi-v2.1"
   ```

### Docker Installation:

1. Build the Docker image:
   ```bash
   docker build -t football-nlu-api .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 football-nlu-api
   ```

## 💻 Usage Examples

### Starting the API:

```bash
# Local run
uvicorn main:app --reload

# With Docker
docker run -p 8000:8000 football-nlu-api
```

### API Endpoints:

#### 1. Basic Health Check:
```bash
curl http://localhost:8000/
```

Response:
```json
{"message": "Hello World"}
```

#### 2. Process Natural Language Query:
```bash
curl -X POST "http://localhost:8000/nlu" \
  -H "Content-Type: application/json" \
  -d '{"message": "When is the next Manchester United match?"}'
```

Response:
```json
{
  "result": {
    "text": "When is the next Manchester United match?",
    "intent": {
      "name": "matches-team_next_match",
      "confidence": 0.92
    },
    "entities": [
      {
        "entity": "team_name",
        "start": 13,
        "end": 30,
        "confidence_entity": 0.97,
        "value": "Manchester United",
        "extractor": "_",
        "value_id": {"team_id": 33, "Score": 0.85}
      }
    ]
  }
}
```

#### 3. Get Team's Next Match:
```bash
curl -X POST "http://localhost:8000/football/team_next_match" \
  -H "Content-Type: application/json" \
  -d '{"team_1_id": 33}'
```

Response:
```json
{
  "results": [
    {
      "match_date": "2022-05-07T14:00:00+00:00",
      "match_timezone": "UTC",
      "team_home": {
        "id": 33,
        "name": "Manchester United",
        "logo": "https://media.api-sports.io/football/teams/33.png"
      },
      "team_away": {
        "id": 51,
        "name": "Brighton",
        "logo": "https://media.api-sports.io/football/teams/51.png"
      },
      "goals": {
        "home": null,
        "away": null
      }
    }
  ]
}
```

## 🏗️ Project Structure

```
FootballFluent 💬⚽-nlu-api/
├── .dockerignore            # Docker ignore file
├── .env                     # Environment variables (not in version control)
├── Dockerfile               # Docker configuration
├── main.py                  # Main application entry point
├── football.py              # Football API integration
├── resourse.py              # ML model loading utilities
├── schemes.py               # Pydantic data models
└── requermint.txt           # Python dependencies
```

### Key Files:
- `main.py`: Contains FastAPI application setup and route handlers
- `football.py`: Functions for interacting with the football API
- `resourse.py`: Handles machine learning model loading and management
- `schemes.py`: Defines data models and team name mappings
- `Dockerfile`: Containerization configuration
- `requermint.txt`: Project dependencies

## 📚 API Documentation

### Endpoints:

#### `GET /`
Health check endpoint that returns a simple message.

**Response:**
```json
{"message": "Hello World"}
```

#### `POST /nlu`
Process natural language text to extract intents and entities.

**Request Body:**
```json
{
  "message": "string"  // The natural language query
}
```

**Response:**
```json
{
  "result": {
    "text": "string",
    "intent": {
      "name": "string",
      "confidence": "float"
    },
    "entities": [
      {
        "entity": "string",
        "start": "integer",
        "end": "integer",
        "confidence_entity": "float",
        "value": "string",
        "extractor": "string",
        "value_id": "object | null"
      }
    ]
  }
}
```

#### `POST /football/team_next_match`
Get the next match for a specified team.

**Request Body:**
```json
{
  "team_1_id": "integer",
  "team_2_id": "integer" // Optional, defaults to -1
}
```

**Response:**
```json
{
  "results": [
    {
      "match_date": "string",
      "match_timezone": "string",
      "team_home": {
        "id": "integer",
        "name": "string",
        "logo": "string"
      },
      "team_away": {
        "id": "integer",
        "name": "string",
        "logo": "string"
      },
      "goals": {
        "home": "integer | null",
        "away": "integer | null"
      }
    }
  ]
}
```

#### `POST /football/team_prev_match`
Get the previous match for a specified team.

**Request Body:**
```json
{
  "team_1_id": "integer",
  "team_2_id": "integer" // Optional, defaults to -1
}
```

**Response:** *Same structure as team_next_match*

### Models:

#### Intent Classification Labels:
- `greet-hi`: Simple greeting
- `greet-who_are_you`: Identity question
- `greet-good_bye`: Farewell
- `matches-team_next_match`: Query about upcoming matches
- `matches-match_time`: Query about match timing
- `matches-match_result`: Query about match results

#### Entity Types:
- `team_name`: Football team name

## ⚙️ Configuration

### Environment Variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `hf_token` | Hugging Face API token for model access | - |
| `football_api` | RapidAPI Football API key | - |
| `setfit_model_id` | Model ID for intent detection | "Ah7med/setfit-football_bootpress_paraph-multi-v2" |
| `gliner_model_id` | Model ID for entity recognition | "urchade/gliner_multi-v2.1" |

### Docker Configuration:
The provided Dockerfile configures:
- Python 3.9 slim as the base image
- Required system dependencies
- Python dependencies from requermint.txt
- Environment variables for the models and APIs
- Exposed port 8000 for the FastAPI application

## 🧪 Testing

Currently, the project doesn't include automated tests. To manually test the API:

1. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

2. Access the FastAPI interactive documentation:
   ```
   http://localhost:8000/docs
   ```

3. Use the interactive UI to test each endpoint with sample data

## 🚢 Deployment

### Docker Deployment:

```bash
docker build -t football-nlu-api .
docker run -p 8000:8000 football-nlu-api
```

### Cloud Deployment:

The API can be deployed to any cloud service that supports Docker containers:

- **AWS**: Deploy as an ECS service or on EC2
- **Google Cloud**: Deploy to Cloud Run or GKE
- **Azure**: Deploy to Azure Container Instances or AKS
- **Heroku**: Deploy using the container registry

Example for AWS ECS:
```bash
# Build and tag the image
docker build -t football-nlu-api .
aws ecr get-login-password --region region | docker login --username AWS --password-stdin your-account-id.dkr.ecr.region.amazonaws.com
docker tag football-nlu-api:latest your-account-id.dkr.ecr.region.amazonaws.com/football-nlu-api:latest
docker push your-account-id.dkr.ecr.region.amazonaws.com/football-nlu-api:latest
```

Then create an ECS task definition and service through the AWS console or CLI.

## 🤝 Contributing Guidelines

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a pull request

### Code Style:
- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Update documentation for new features

## ⚖️ License Information

This project is released under the MIT License.

```
MIT License
```

## 👏 Acknowledgments

- [SetFit](https://github.com/huggingface/setfit) - Few-shot text classification
- [GLiNER](https://github.com/urchade/GLiNER) - General Language understanding model for Named Entity Recognition
- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [RapidAPI Football API](https://rapidapi.com/api-sports/api/api-football/) - Comprehensive football data

## ❓ FAQ Section

### How do I get API keys?
- **Hugging Face**: Register at [Hugging Face](https://huggingface.co/), then generate a token in your account settings
- **RapidAPI Football**: Register at [RapidAPI](https://rapidapi.com/), subscribe to the API-Football service, and copy your API key

### Why is my model loading slowly?
The first time you run the application, the ML models will be downloaded from Hugging Face. This only happens once, and subsequent startups will be faster.

### Can I use different ML models?
Yes, you can specify different models for intent classification and entity recognition by setting the `setfit_model_id` and `gliner_model_id` environment variables.

### How many API calls can I make?
API limits depend on your RapidAPI Football API subscription tier. Check your subscription details for specific limits.

## 📝 Changelog

### v1.0.0 (2023-01-01)
- Initial release
- Basic NLU capabilities for football queries
- Team entity recognition
- Match information retrieval

## 📬 Contact Information

- **Linked In**: [Hamedo](https://www.linkedin.com/in/ahmed-mahmoud-80356b220/)
-

Feel free to reach out with questions, suggestions, or contributions!
