from flask import Flask, session, redirect, url_for, escape, request, app, g, send_file, send_from_directory
import random, os
from termcolor import colored

variable = 100000
print(colored('*** VARIABLE = ', 'green'), variable)
from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache()
app = Flask(__name__)
app.secret_key = "very_secret_key_do_not_steal_bitcoins"

#
# Keeping session stuff
#

@app.route('/', methods=['GET'])
def index():
    print(colored('*** def INDEX()', 'green'))
    global variable
    variable = variable + 1
    if 'variable' not in g:
        g.variable = 1
    else:
        g.variable = g.variable + 1

    print(colored('*** g.variable = ', 'green'), g.variable)
    rv = cache.get('frame')
    if rv is None:
        cache.set('frame', 1, timeout=5 * 60)
    else:
        cache.set('frame', rv + 1, timeout=5 * 60)
    return '{"g.variable": "' + str(cache.get('frame')) + '"}'
    if session.get('id'):
        id = session['id']
        return '<html>' + \
               '<h3>Session section:</h3>' + \
               'Current session id: <span style="color: red">' + id + '</span>' +\
               f'<br><a href={ url_for("drop_session") }>Destroy session</a>' +\
               '<h3>Chat bot API:</h3>' +\
               f'<a href={ url_for("bot_get_state_and_data") }>Send GET request at "/bot/get_state_and_data"</a>' +\
               '<br><a>Send POST request at "/bot/publish_message"</a>' +\
               '</html>'
    else:
        return redirect(url_for('new_session'))

@app.route('/new_session', methods=['GET'])
def new_session():
    print(colored('*** def new_session()', 'green'))
    global variable
    variable = variable + 1
    if 'variable' not in g:
        g.variable = 1
    else:
        g.variable = g.variable + 1

    print(colored('*** g.variable = ', 'green'), g.variable)
    rv = cache.get('frame')
    if rv is None:
        cache.set('frame', 1, timeout=5 * 60)
    else:
        cache.set('frame', rv + 1, timeout=5 * 60)
    return '{"g.variable": "' + str(cache.get('frame')) + '"}'
    if not session.get('id'):
        session['id'] = str(random.uniform(0,1)) # create unique ID for user
    return redirect(url_for('index'))

@app.route('/drop_session', methods=['GET'])
def drop_session():
    print(colored('*** def drop_session()', 'green'))
    global variable
    variable = variable + 1
    if 'variable' not in g:
        g.variable = 1
    else:
        g.variable = g.variable + 1

    print(colored('*** g.variable = ', 'green'), g.variable)
    rv = cache.get('frame')
    if rv is None:
        cache.set('frame', 1, timeout=5 * 60)
    else:
        cache.set('frame', rv + 1, timeout=5 * 60)
    return '{"g.variable": "' + str(cache.get('frame')) + '"}'
    if session.get('id'):
        session.pop('id', None)
        return redirect(url_for('finish'))
    # return redirect(url_for('index'))

@app.route('/end', methods=['GET'])
def finish():
    print(colored('*** def finish()', 'green'))
    global variable
    variable = variable + 1
    if 'variable' not in g:
        g.variable = 1
    else:
        g.variable = g.variable + 1

    print(colored('*** g.variable = ', 'green'), g.variable)
    rv = cache.get('frame')
    if rv is None:
        cache.set('frame', 1, timeout=5 * 60)
    else:
        cache.set('frame', rv + 1, timeout=5 * 60)
    return '{"g.variable": "' + str(cache.get('frame')) + '"}'
    if session.get('id'):
        return redirect(url_for('index'))
    else:
        return f"Thank you for using our bot!<br><a href={ url_for('index') }>Open up new chat</a>"

#
# An actual chat bot API
#

@app.route('/bot/get_state_and_data', methods=['GET'])
def bot_get_state_and_data():
    print(colored('*** def bot_get_state_and_data()', 'green'))
    global variable
    variable = variable + 1
    if 'variable' not in g:
        g.variable = 1
    else:
        g.variable = g.variable + 1
    print(colored('*** g.variable = ', 'green'), g.variable)
    rv = cache.get('frame')
    if rv is None:
        cache.set('frame', 1, timeout=5 * 60)
    else:
        cache.set('frame', rv + 1, timeout=5 * 60)
    return '{"g.variable": "' + str(cache.get('frame')) + '"}'
    if session.get('id'):
        id = session['id']
        return '{"id": "' + id + '", "other": "data"}'
    else:
        return '{"id": null, "error": "no session found"}'

@app.route('/bot/publish_message', methods=['POST'])
def bot_publish_message():
    print(colored('*** def bot_publish_message()', 'green'))
    global variable
    variable = variable + 1
    if 'variable' not in g:
        g.variable = 1
    else:
        g.variable = g.variable + 1
    print(colored('*** g.variable = ', 'green'), g.variable)
    rv = cache.get('frame')
    if rv is None:
        cache.set('frame', 1, timeout=5 * 60)
    else:
        cache.set('frame', rv + 1, timeout=5 * 60)
    return '{"g.variable": "' + str(cache.get('frame')) + '"}'
    if session.get('id'):
        id = session['id']
        return '{"id": "' + id + '", "status": "success"}'
    else:
        return '{"id": null, "error": "no session found"}'

@app.route('/getCoord', methods=['GET'])
def getCoord():
    print(colored('*** def new_session()', 'green'))
    return '{"detected":[{"lat": "55.33568", "lon": "155.57457"},{"lat": "53.48181", "lon": "160.47447"}]}'
# global variable = 100500

@app.route('/download/<filename>', methods=['GET','POST'])
def download(filename):
    uploads = os.path.join(app.root_path, "files")
    print('*** uploads = ', uploads)
    return send_from_directory(directory=uploads, filename=filename)

@app.route("/downloadfile/<filename>")
def downloadfile (filename = None):
    if filename is None:
        self.Error(400)
    try:
        rt_path = current_app.root_path
        return send_file(rt_path + "/files/"+filename, as_attachment=True)
    except Exception as e:
        self.log.exception(e)
        self.Error(400)

if __name__ == '__main__':
    print(colored('*** STARTING SERVER ***', 'green'))
    #global variable
    variable = 100500
    print(colored('*** VARIABLE = ', 'green'), variable)
    app.run(debug=True, host='0.0.0.0')
 