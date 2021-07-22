from xml.dom import minidom
import xml.etree.ElementTree as ET
import os

# parse an xml file by name
mydoc = minidom.parse('annotations.xml')
tree = ET.parse('annotations.xml')
root = tree.getroot()

items = mydoc.getElementsByTagName('image')

# one specific item attribute
print('Item #2 attribute:')
#print(items[1].attributes['name'].value)

for elem in root.iter('image'):
    '''
    filename = elem.attributes['name'].value
    from_video = filename.split('/')[1][:-4]
    frame = filename.split('/')[2]

    image_loc = os.path.join('',from_video + '_' + frame)
    elem.set('name', )
    '''
    
    filename = elem.get('name')
    from_video = filename.split('/')[1][:-4]
    frame = filename.split('/')[2]

    image_loc = os.path.join('',from_video + '_' + frame)
    
    elem.set('name',image_loc )
    print("image_loc",image_loc," set: ",filename)

tree.write('annotations.xml')

# all item attributes
print('\nAll attributes:')
for elem in items:
    #print(elem.attributes['name'].value)
    
    filename = elem.attributes['name'].value
    from_video = filename.split('/')[1][:-4]
    frame = filename.split('/')[2]

    image_loc = os.path.join('',from_video + '_' + frame)
    #print("image_loc:",image_loc)
    #elem.set('name',image_loc)
    #image['file_name'] = str(image_loc)
    #print(image['file_name'])
    #count+=1

    #print(elem.attributes['name'].value)

# one specific item's data
print('\nItem #2 data:')
#print(items[1].firstChild.data)
#print(items[1].childNodes[0].data)

# all items data
print('\nAll item data:')
#for elem in items:
#    print(elem.firstChild.data)
