from os import environ as env

class Config:
    
    POSTGRES_USER = env.get('POSTGRES_USER')
    POSTGRES_PASSWORD = env.get('POSTGRES_PASSWORD')
    POSTGRES_HOST = env.get('POSTGRES_HOST')
    POSTGRES_PORT = env.get('POSTGRES_PORT')
    POSTGRES_DATABASE = env.get('POSTGRES_DB')
    URI = env.get('DATABASE_URL', f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}')
    SQLALCHEMY_DATABASE_URI = URI.replace("postgres://", "postgresql://", 1) if URI.startswith("postgres://") else URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = env.get('SECRET_KEY')
    PORT = int(env.get('PORT', 5000))