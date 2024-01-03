
from app import app
from models import db_session
from config import Config

def run_app():
    app.config.from_object(Config)
    try:
        app.run()
    except Exception as e:
        print("Failed to run the app: ", e)
    finally:
        db_session.remove()

if __name__ == "__main__":
    run_app()

