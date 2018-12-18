import xmltodict
import os

vboxConfig = """C:\Users\Optiplex 9010\.VirtualBox\VirtualBox2.xml"""

# file:     VirtualBox.xml main config file
# uuid:     machine id to update vm disk location
# src:      new vm disk src directory
# returns:  xml to be stored to file
def updateSrc(file, uuid, src):
    with open(file) as fd:
        doc = xmltodict.parse(fd.read())
        x = 0
        for x in range(len(doc['VirtualBox']['Global']['MachineRegistry'])):
            for row in doc['VirtualBox']['Global']['MachineRegistry']['MachineEntry']:
                if row['@uuid'] == uuid:
                    row['@src'] = src
                print row['@uuid']+'\t'+row['@src']
    output = (xmltodict.unparse(doc, pretty=True))
    return output

# file:     VirtualBox.xml main config file
# uuid:     machine id to update vm disk location
def getName(file, uuid):
    with open(file) as fd:
        doc = xmltodict.parse(fd.read())
        x = 0
        for x in range(len(doc['VirtualBox']['Global']['MachineRegistry'])):
            for row in doc['VirtualBox']['Global']['MachineRegistry']['MachineEntry']:
                if row['@uuid'] == uuid:
                    print row['@uuid']+'\t'+row['@src']
                    targetVbox = str(row['@src']).rsplit("""\\""",1)[0]+'\\'
                    print targetVbox
                    machCfg = find('.vbox', targetVbox)
    with open(machCfg) as fd:
        doc = xmltodict.parse(fd.read())
        name =doc['VirtualBox']['Machine']['@name']
        print name
        return name


def find(pattern, path):
    for file in os.listdir(path):
        if file.endswith(pattern):
            print "Found config file:" + str(file)
            return(os.path.join(path, file))

getName(vboxConfig,"{4b08775c-2117-4769-9429-d7e6f5859154}")
# updateSrc("""C:\Users\Optiplex 9010\.VirtualBox\VirtualBox2.xml""","{d8f99551-4e5f-43f7-991a-119b046d8013}", """C:\New""")
# outputFile = open("out.xml", "w")
# outputFile.write(output)
# outputFile.close()#