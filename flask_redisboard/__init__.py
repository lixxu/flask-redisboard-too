#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

try:
    from werkzeug.urls import url_quote_plus
except ImportError:
    from urllib.parse import quote_plus as url_quote_plus

from .redisboard import module


class RedisBoardExtension:
    def __init__(self, app: Flask = None) -> None:
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        for k, v in self._default_config().items():
            app.config.setdefault(k, v)

        if not app.config.get("SECRET_KEY"):
            raise RuntimeError(
                "The Flask-RedisBoard requires the 'SECRET_KEY' config var to be set"
            )

        app.jinja_env.filters["quote_plus"] = url_quote_plus
        app.register_blueprint(module, url_prefix="/redisboard")

    def _default_config(self) -> None:
        return {
            "REDIS_HOST": "localhost",
            "REDIS_PORT": 6379,
            "REDIS_PASSWORD": None,
            "REDIS_UNIX_SOCKET_PATH": None,
            "REDISBOARD_SOCKET_TIMEOUT": None,
            "REDISBOARD_SOCKET_CONNECT_TIMEOUT": None,
            "REDISBOARD_SOCKET_KEEPALIVE": None,
            "REDISBOARD_SOCKET_KEEPALIVE_OPTIONS": None,
            "REDISBOARD_SLOWLOG_LEN": 100,
        }
