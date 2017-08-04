import re
import web
import time
from index import index
import explorerhat as ehat

render = web.template.render('templates/')

urls = (
    '/led', 'blink',
    '/forward', 'forward',
    '/reverse', 'reverse',
    '/right', 'right',
    '/left', 'left',
    '/move', 'move',
    '/stop', 'stop',
    '/', 'home',
    '/(.*)', 'index'
)
app = web.application(urls, globals())

class blink:        
    def GET(self):
        ehat.light.green.on()
        time.sleep(1)
        ehat.light.green.off()

        web.header('cache-control', 'private, max-age=0, no-cache', unique=True)
        return 'LED Working!'

class forward:
    def GET(self):
        print 'IN HERE'
        ehat.motor.forwards(100)
        time.sleep(1)
        ehat.motor.speed(0)

class reverse:
    def GET(self):
        ehat.motor.backwards(100)
        time.sleep(1)
        ehat.motor.speed(0)

class right:
    def GET(self):
        ehat.motor.one.forwards(50)
        ehat.motor.two.backwards(50)
        time.sleep(1)
        ehat.motor.speed(0)

class left:
    def GET(self):
        ehat.motor.one.backwards(50)
        ehat.motor.two.forwards(50)
        time.sleep(1)
        ehat.motor.speed(0)

class move:
    def POST(self):
        data = web.data()
        print(data)
        matchx = re.search(r'x=([^&]*)', data)
        x = int(matchx.group(1))
        matchy = re.search(r'y=([^&]*)', data)
        y = int(matchy.group(1))
        ehat.motor.one.speed(x + y)
        ehat.motor.two.speed(y - x)
        ehat.light.red.on()

class stop:
    def POST(self):
        ehat.motor.speed(0)
        ehat.light.red.off()
        

if __name__ == "__main__":
    app.run()
