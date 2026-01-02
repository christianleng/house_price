# Commandes Utiles pour le Projet House Price

## Affichage de l'arborescence

```bash
# Affiche l'arborescence du dossier app/ en excluant les caches Python
tree app/ -I '*pycache*'
```

# Accéder à la base de données PostgreSQL

docker exec -it ${DB_CONTAINER_NAME} psql \
 -U ${POSTGRES_USER} \
 -d ${POSTGRES_DB}

# Exécuter un script SQL

docker exec -i ${DB_CONTAINER_NAME} psql \
 -U ${POSTGRES_USER} \
 -d ${POSTGRES_DB} < test.sql

# Lister toutes les tables

docker exec -it ${DB_CONTAINER_NAME} psql \
 -U ${POSTGRES_USER} \
 -d ${POSTGRES_DB} \
 -c "\dt"
