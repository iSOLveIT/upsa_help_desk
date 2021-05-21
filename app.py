import os
from content import app


app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


if __name__ == '__main__':
    app.run()
