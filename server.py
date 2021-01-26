import os
import sentry_sdk
from bottle import run, route, HTTPResponse
from sentry_sdk.integrations.bottle import BottleIntegration

# Enter your Sentry link here
SENTRY_DSN = 'https://e931839b0cf64cfc82316d36e95f307f@o505450.ingest.sentry.io/5593753'

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[BottleIntegration()]
)

@route('/')
def im_ok():
    response = HTTPResponse(status=200, body='I am OK')
    return response

@route('/success')
def get_success():
    response = HTTPResponse(status=200, body='OK')
    return response

@route('/fail')
def get_error():
    raise RuntimeError('Server error for the test')

if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        server='gunicorn',
        workers=3
    )
else:
    run(
        host='localhost',
        port=8080,
        debug=True
    )