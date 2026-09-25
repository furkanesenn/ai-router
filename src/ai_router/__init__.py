from . import cli

from .api.models import startup  

app = cli.app
main = app

startup.initalize_models() # Initialize models on startup

if __name__ == "__main__":
    main()