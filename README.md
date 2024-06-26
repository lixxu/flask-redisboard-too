# flask-redisboard

A flask extension to support user view and manage redis with beautiful interface.

## Preview

<table align="center">
    <tr>
        <td align="center">
            <a href="https://raw.githubusercontent.com/hjlarry/flask-redisboard/master/screenshot/demo1.png">
                <img src="screenshot/demo1.png" alt="Screenshot Dashboard" width="480px" />
            </a>
        </td>
        <td align="center">
            <a href="https://raw.githubusercontent.com/hjlarry/flask-redisboard/master/screenshot/demo2.png">
                <img src="screenshot/demo2.png" alt="Screenshot Database" width="480px" />
            </a>
        </td>
    </tr>
    <tr>
        <td align="center">
            <a href="https://raw.githubusercontent.com/hjlarry/flask-redisboard/master/screenshot/demo3.png">
                <img src="screenshot/demo3.png" alt="Screenshot Command" width="480px" />
            </a>
        </td>
        <td align="center">
            <a href="https://raw.githubusercontent.com/hjlarry/flask-redisboard/master/screenshot/demo4.png">
                <img src="screenshot/demo4.png" alt="Screenshot ServerInfo" width="480px" />
            </a>
        </td>
    </tr>
</table>

## Get Started

Installation is easy:

~~~bash
pip install flask-redisboard-too
~~~

### Try to run

Just type command:

~~~bash
redisboard
~~~

### Run in flask

Initialize the extension:

~~~python
from flask_redisboard import RedisBoardExtension
...
board = RedisBoardExtension(app)
~~~

Also support for factory pattern:

~~~python
from flask_redisboard import RedisBoardExtension
from flask import Flask

board = RedisBoardExtension()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '123456'
    board.init_app(app)
    app.run()


if __name__ == '__main__':
    create_app()
~~~

Now, you can go to 127.0.0.1:5000/redisboard
