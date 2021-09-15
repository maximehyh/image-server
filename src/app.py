from dotenv import load_dotenv
load_dotenv()
from server.config import SERVER_PORT, DEBUG  # noqa: E402
from server.routes import create_app  # noqa: E402

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=SERVER_PORT, debug=DEBUG)
