from reactpy import component, html, hooks
from reactpy.backend.flask import configure
from flask import Flask
import json

@component
def Heading():
    return html.div(
        html.h1("Hello, world!"),
        html.div({'id': 'analytics'}),
        html.hr()
    )

@component
def ClickCounter():
    clicks, set_clicks = hooks.use_state(0)

    def handle_click(event):
        i = -1 if event['shiftKey'] else 1
        set_clicks(clicks + i)

    return html.div(
        html.h2('Clicks: ' + str(clicks)),
        html.button({
            'on_click': handle_click,
        }, 'Clicks++ (hold shift for clicks--)')
    )

@component
def EventTest():
    eventData, set_eventData = hooks.use_state("")

    def handle_click(event):
        set_eventData(json.dumps(event, indent=2))

    return html.div(
        html.h3('Event Tester'),
        html.pre(eventData),
        html.button({'on_click': handle_click}, 'Trigger Event')
    )
    

@component
def App():
    return html.div(
        Heading(),
        html.br(),
        ClickCounter(),
        html.br(),
        EventTest(),

        html.script({
            'src': 'https://analytics.marcusj.tech/analytics.js',
            'defer': True,
            'show': True,
            'onload': 'showAnalytics()'
        })
    )

app = Flask(__name__)
configure(app, App)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)