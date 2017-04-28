################################################################################
#----------------MyWiki---by-Brian-Evans---------------------------------------#
################################################################################

from bottle import route, run, template, static_file, post, request, get
import os.path

#####---------------------Main-page-view-functions-------------------------#####

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
    #pagedata is a string
    pagedata = request.forms.get('PageData')
    pagedata = stripHTML(pagedata)
    pagedata = alinkbuild(pagedata)
    fo = open('./content/' + pagename, 'w')
    fo.write(pagedata)
    fo.close()
    return template('editcomplete', pagename=pagename)

@route('/edit/existing/<pagename>')
def editExisting(pagename):
    with open('./content/' + pagename, 'r') as textfile:
        bodytext = textfile.read()
        bodytext = alinkunbuild(bodytext)
    return template('editexisting', pagename=pagename, bodytext=bodytext)


@route('/styles/<css>')
def servestyle(css):
    return static_file(css,root='./styles/')





#####-------------Functions-for-editor(s)/String-Functions-----------------#####

def alinkbuild(string):
#Will build hyperlinks from WikiCode entered into the edit textareabox
#which will allow
    instances = string.count('[F: ')
    if instances > 0:
        for x in range(instances):
            start = string.find('[F: ') + 4
            end = string.find(' :F]')
            linktext = string[start:end]
            linkname = linktext.replace(' ','_')
            string = string.replace('[F: ' + linktext + ' :F]', '<a href="/wiki/' + linkname + '">' + linktext + '</a>')
        return string
    else:
        return string

def alinkunbuild(string):
#Deconstructs hyperlinks back into Wikicode for the edit textarea box
    instances = string.count('<a href=')
    if instances > 0:
        for x in range(instances):
            start = string.lower().find('<a href=')
            end = string.find('>',start + 1) + 1
            linktext = string[start:end]
            string = string.replace(linktext,'[F: ')
            start = string.lower().find('</a>')
            linktext = string[start:start + 4]
            string = string.replace(linktext,' :F]')
        return string
    else:
        return string

def stripHTML(string):
#Will strip all html tags from a string
    instances = string.count('<')
    if instances > 0:
        for x in range(instances):
            start = string.find('<')
            end = string.find('>') + 1
            linktext = string[start:end]
            string = string.replace(linktext,'').replace('  ',' ')
        return string
    else:
        return string

def swapScript(string):
    #Swaps html for wikiCode and vice versa
    tags = {'<b>':'[b: ','</b>':' b:]','<i>':'[i: ','</i>':' :i]','<sub>':'[s: ','</sub>':' :s]','<sup>':'[S: ','</sup>':' :S]','<blockquote>':'[q: ','</blockquote>':' :q]','<p>':'[p: ','</p>':' :p]'}
    '''More stuff goes here to do the swapping,
    but I've gotta punch the clock right now. I'll do it later.'''

#####---------------------------Run-the-server-----------------------------#####
if __name__ == '__main__':
    run(host='localhost', port=8080)
