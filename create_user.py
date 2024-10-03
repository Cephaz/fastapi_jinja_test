import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.models import User
from app.database import Base

# Charger les variables d'environnement
load_dotenv()

# Récupérer l'URL de la base de données
DATABASE_URL = os.getenv("DATABASE_URL")

# Créer le moteur de base de données
engine = create_engine(DATABASE_URL)

# Créer une session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

# Créer un nouvel utilisateur
new_user = User(
    username="testudwdwser",
    email="testudwqser@examdwqple.com",
    hashed_password="hashed_passdwqword_here",  # Dans un vrai scénario, vous hacheriez le mot de passe
)

# Ajouter l'utilisateur à la session
db.add(new_user)

# Commit la transaction
db.commit()

# Rafraîchir l'instance pour obtenir l'ID généré
db.refresh(new_user)

print(f"Nouvel utilisateur créé avec l'ID: {new_user.id}")

# Fermer la session
db.close()
