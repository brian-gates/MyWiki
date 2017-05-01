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
    #PageData is a string
    pagedata = request.forms.get('PageData')
    pagedata = stripHTML(pagedata)
    pagedata = alinkbuild(pagedata)
    pagedata = swapScript(pagedata,'ToHTML')
    fo = open('./content/' + pagename, 'w')
    fo.write(str.strip(pagedata))
    fo.close()
    return template('editcomplete', pagename=pagename)

@route('/edit/existing/<pagename>')
def editExisting(pagename):
    with open('./content/' + pagename, 'r') as textfile:
        bodytext = textfile.read()
        bodytext = alinkunbuild(bodytext)
        bodytext = swapScript(bodytext,'FromHTML')
        bodytext = str.strip(bodytext)
    return template('editexisting', pagename=pagename, bodytext=bodytext)


@route('/styles/<css>')
def servestyle(css):
    return static_file(css,root='./styles/')





#####-------------Functions-for-editor(s)/String-Functions-----------------#####

def alinkbuild(string):
#Will build hyperlinks from WikiCode entered into the edit textareabox
#At present this allows for properly nested wikiCode within '[F: ... :F]' tags
    instances = string.count('[F: ')
    if instances > 0:
        for x in range(instances):
            start = string.find('[F: ') + 4
            end = string.find(' :F]')
            linktext = string[start:end]
            if linktext.count(':') > 1 and linktext.count(':') % 2 == 0:
                counter = linktext.count(':')/2
                linkname = linktext[4*counter:len(linktext)-4*counter]
                linkname = linkname.replace(' ','_')
            else:
                linkname = linktext.replace(' ','_')
            string = string.replace('[F: ' + linktext + ' :F]', '<a href="/wiki/' + linkname + '">' + linktext + '</a>')
        return string
    else:
        return string

def alinkunbuild(string):
#Deconstructs hyperlinks back into Wikicode for the edit textarea box
    instances = string.lower()
    instances = string.count('<a href=')
    print instances
    if instances > 0:
        for x in range(instances):
            start = string.lower().find('<a href=')
            end = string.find('>',start + 1) + 1
            linktext = string[start:end]
            string = string.replace(linktext,'[F: ')
            string = string.replace('</a>',' :F]')
        print string
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

def swapScript(string,direction='FromHTML'):
    #Direction takes: 'FromHTML' and any other value (to go ToHTML)
    #Swaps html for wikiCode and vice versa
    tags = [
    ['<b>','[b: '],['</b>',' :b]'],
    ['<i>','[i: '],['</i>',' :i]'],
    ['<sub>','[s: '],['</sub>',' :s]'],
    ['<sup>','[S: '],['</sup>',' :S]'],
    ['<blockquote>','[q: '],['</blockquote>',' :q]'],
    ['<p>','[p: '],['</p>',' :p]']
    ]

    for x in tags:
        if direction == 'FromHTML':
            string = string.replace(x[0],x[1])
        else:
            string = string.replace(x[1],x[0])
    return string


#####---------------------------Run-the-server-----------------------------#####
if __name__ == '__main__':
    run(host='localhost', port=8080)
