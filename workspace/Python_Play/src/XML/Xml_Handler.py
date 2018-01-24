'''
Created on Oct 12, 2015

@author: marshall
'''

from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

class Xml_Handler(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        
    ### this is just playground for dealing with xml doc's in python
    ####
    ## Creating a XML file
    ####
    def create_xml(self):
    
        # <membership/>
        membership = Element( 'membership' )
    
        # <membership><users/>
        users = SubElement( membership, 'users' )
    
        # <membership><users><user/>
        SubElement( users, 'user', name='john' )
        SubElement( users, 'user', name='charles' )
        SubElement( users, 'user', name='peter' )
    
        # <membership><groups/>
        groups = SubElement( membership, 'groups' )
    
        # <membership><groups><group/>
        group = SubElement( groups, 'group', name='users' )
    
        # <membership><groups><group><user/>
        SubElement( group, 'user', name='john' )
        SubElement( group, 'user', name='charles' )
    
        # <membership><groups><group/>
        group = SubElement( groups, 'group', name='administrators' )
    
        # <membership><groups><group><user/>
        SubElement( group, 'user', name='peter' )
    
        output_file = open( 'membership_1.xml', 'w')
        output_file.write( '<?xml version="1.0"?>')
        output_file.write ( ElementTree.tostring( membership))
        output_file.close()
    

    ####
    ## reading xml doc
    ####
    def read_xml(self):
    
        document = ElementTree.parse( 'memmbership.xml')
        users = document.find( 'users')
    
        print "here are the users:"
        print users
        ### quickly get  user nodes
        for user in document.findall( 'users/user'):
            print user.attrib[ 'name']
    
        ### Iterating elements
        for group in document.findall( 'groups/group' ):
            print 'Group:', group.attrib[ 'name' ]
            print 'Users:'
            for node in group.getchildren():
                if node.tag == 'user':
                    print '-', node.attrib[ 'name' ]
    
    
        ### visit every single element from starting point
    
        users = document.find( 'users' )
        for node in users.getiterator():
            print node.tag, node.attrib, node.text, node.tail
    
        ## Produces this output:
        ## users {} None None
        ## user {'name': 'john'} None None
        ## user {'name': 'charles'} None None
        ## user {'name': 'peter'} None None
        ## iterate only children.
    
        users = document.find( 'users' )
        for node in users.getchildren():
            print node.tag, node.attrib, node.text, node.tail
    
        ## Produces this output:
    
        ## user {'name': 'john'} None None
        ## user {'name': 'charles'} None None
        ## user {'name': 'peter'} None None

if __name__ == "__main__":
    import sys
    
    handle = Xml_Handler.read_xml()
    print handle
    sys.exit()

