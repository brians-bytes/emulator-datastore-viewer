import os

from viewer import app


def main():
    port = os.environ.get('PORT', 5000)
    host = os.environ.get('HOST', 'localhost')
    app.run(host=host, port=port, debug=True)


if __name__ == '__main__':
    main()
