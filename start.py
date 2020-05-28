from api.routers import app
from utils.get_configs import system_configs
if __name__ == "__main__":
    app.run(host=system_configs['host'], port=system_configs['port'], debug=True)
