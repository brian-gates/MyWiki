from bottle import route, run, template, static_file, post, request, get, redirect
import os.path


@route('/wiki/<pagename>')
def build(pagename='main'):
    if not os.path.isfile('./content/' + str(pagename)):
        return template('editcreate', pagename=pagename)
    else:
        with open('./content/' + pagename, 'r') as textfile:
            bodytext = textfile.read()
        return template('core', pagename=pagename, bodytext=bodytext)

@route('/edit/<pagename>', method='POST')
def createedit(pagename):
    #pagedata == string
    pagedata = request.forms.get('PageData')
    
    fo = open('./content/' + pagename, 'w')
    fo.write(pagedata)
    fo.close()
    return template('editcomplete', pagename=pagename)

@route('/styles/<css>')
def servestyle(css):
    return static_file(css,root='./styles/')


if __name__ == '__main__':
    run(host='localhost', port=8080)
