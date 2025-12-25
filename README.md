source .venv/bin/activate
pip install -r requirements.txt
fastapi dev main.py

docker compose build
docker compose up -d
docker compose logs -f
docker compose logs -f fastapi

{
"name": "Jean Dupont",
"agency_name": "Dupont Immobilier",
"email": "jean.dupont@agency.com",
"phone": "0601020304",
"password": "SecurePass123",
"rsac_number": "RSAC123456789",
"city": "Paris"
}
