#!env/bin/python3
from flask import Flask
from markupsafe import escape
import prometheus_client as prom
from prometheus_client import Counter, make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware

prom.REGISTRY.unregister(prom.PROCESS_COLLECTOR)
prom.REGISTRY.unregister(prom.PLATFORM_COLLECTOR)
prom.REGISTRY.unregister(prom.GC_COLLECTOR)

app = Flask(__name__)

world_metric = Counter('world', 'hello to world')
user_metric = Counter('user', 'hello to user', ['user'])


@app.route("/")
def hello_world():
    world_metric.inc()
    return "<p>Hello, World</p>"

@app.route("/user/<username>")
def hello(username):
    user_metric.labels(user=username).inc()
    return f"Hello, {escape(username)}!"

@app.route("/org/<org_name>")
def hello_from_org(org_name):
    return f"Hello World from {escape(org_name)}!"

@app.route("/org/<org_name>/user/<username>")
def hello_from_org_to_user(org_name, username):
    return f"Hello {escape(username)} from {escape(org_name)}!"

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})
