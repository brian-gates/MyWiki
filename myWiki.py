from bottle import route, run, template, static_file, post, request, get, redirect
import os.path


@route('/wiki/<pagename>')
def build(pagename='main'):
    if not os.path.isfile('./content/' + str(pagename)):
        return template('editcreate', pagename=pagename)
    else:
        return static_file(pagename,root='./content/')

@route('/edit/<pagename>', method='POST')
def createedit(pagename):
    pagedata = request.forms.get('PageData')
    #pagename = request.forms.get()
    fo = open('./content/' + pagename, 'w')
    fo.write(pagedata)
    fo.close()
    return template('editcomplete', pagename=pagename)



if __name__ == '__main__':
    run(host='localhost', port=8080)
