# ShopMind — AI-Powered Natural Language Shopping Assistant

## Chosen Vertical
**Retail & E-Commerce**: Intelligent personalization and shopping experience enhancement.

## Problem Statement
Shoppers waste time filtering through irrelevant products. Search bars are keyword-limited and
context-blind. ShopMind replaces the search bar with a conversational assistant that understands
natural language intent, budget, occasion, and preferences — returning ranked products with
transparent "why this" explanations.

## Approach & Logic

### How It Works
1. User submits a natural language query (e.g., "blue formal shirt under ₹1500 for an interview").
2. The query is sent to the `/api/chat` endpoint.
3. **Gemini** (via Vertex AI) parses the query and extracts structured filters:
   - category, color, max_price, occasion, keywords
4. Extracted filters are used to query the **Firestore** product catalog.
5. Gemini generates a ranked response with a personalized "why this" explanation per product.
6. The frontend renders results in an accessible, keyboard-navigable UI.

### Session Memory
User preferences are tracked in-memory per session ID. Follow-up queries like
"now show me something cheaper" resolve against the previous context.

## Tech Stack
| Component | Service |
|---|---|
| AI / NLP | Gemini 1.5 Flash (Vertex AI) |
| Database | Google Cloud Firestore |
| Backend | FastAPI (Python 3.11, async) |
| Frontend | Vanilla HTML/CSS/JS (accessible, ARIA-compliant) |
| Deployment | Google Cloud Run via Docker |

## How We Hit the 6 Evaluation Criteria

| Criterion | Implementation |
|---|---|
| **Code Quality** | Pydantic v2 models, strict type hints, modular FastAPI routers, PEP8 throughout |
| **Security** | All secrets via `os.getenv` / `.env`, CORS middleware, zero PII in logs, no raw keys in code |
| **Efficiency** | Async FastAPI endpoints, Firestore composite indexes, TTLCache for duplicate Gemini queries |
| **Testing** | pytest suite covering Gemini intent parser and Firestore filter logic with mocks |
| **Accessibility** | Semantic HTML5, `aria-label` on all controls, WCAG AA contrast, full keyboard navigation |
| **Google Services** | Gemini 1.5 Flash (Vertex AI), Cloud Firestore, Cloud Run deployment |

## Assumptions
- Product catalog is pre-seeded via `seed_firestore.py` (50 mock products).
- Prices are in INR (₹).
- Gemini responses are cached for 5 minutes per unique query string to reduce API cost.
- No user authentication required for MVP; session is managed via browser-generated UUID.
- Firestore collection: `products` with composite index on `(category, price, color)`.

## Local Setup

```bash
# 1. Clone and install
pip install -r requirements.txt

# 2. Set environment variables
cp .env.example .env
# Fill in GCP_PROJECT_ID, VERTEX_LOCATION, GOOGLE_APPLICATION_CREDENTIALS

# 3. Seed the database
python seed_firestore.py

# 4. Run locally
uvicorn app.main:app --reload --port 8080

# 5. Run tests
pytest tests/ -v
```

## Cloud Run Deployment

```bash
gcloud builds submit --tag gcr.io/$PROJECT_ID/shopmind
gcloud run deploy shopmind \
  --image gcr.io/$PROJECT_ID/shopmind \
  --platform managed \
  --region asia-south1 \
  --allow-unauthenticated \
  --set-env-vars GCP_PROJECT_ID=$PROJECT_ID,VERTEX_LOCATION=asia-south1
```
