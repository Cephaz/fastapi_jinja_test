# test_connection.py

from alembic.config import Config
from sqlalchemy import create_engine


def test_db_connection():
    # Charger la configuration d'Alembic
    alembic_cfg = Config("alembic.ini")

    # Récupérer l'URL de la base de données depuis la configuration
    db_url = alembic_cfg.get_main_option("sqlalchemy.url")

    # Créer un moteur SQLAlchemy pour tester la connexion
    engine = create_engine(db_url)

    # Tenter de se connecter à la base de données
    try:
        with engine.connect() as connection:
            print("Connexion réussie à la base de données.")
            # Optionnel : vous pouvez exécuter une requête simple pour vérifier
            result = connection.execute("SELECT 1")
            for row in result:
                print("Test de requête réussie:", row)
    except Exception as e:
        print("Erreur de connexion à la base de données:", str(e))


if __name__ == "__main__":
    test_db_connection()
