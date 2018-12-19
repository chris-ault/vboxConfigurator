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

def getVboxLocation(file, uuid):
    with open(file) as fd:
        doc = xmltodict.parse(fd.read())
        x = 0
        for x in range(len(doc['VirtualBox']['Global']['MachineRegistry'])):
            for row in doc['VirtualBox']['Global']['MachineRegistry']['MachineEntry']:
                if row['@uuid'] == uuid:
                    return row['@src'].encode('ascii')
def getUUIDS(file):
    with open(file) as fd:
        doc = xmltodict.parse(fd.read())
        x = 0
        uuids = []
        for x in range(len(doc['VirtualBox']['Global']['MachineRegistry'])):
            for row in doc['VirtualBox']['Global']['MachineRegistry']['MachineEntry']:
                uuids.append(row['@uuid'].encode('ascii'))
        return uuids

# file:     VirtualBox.xml main config file
# uuid:     machine id to update vm disk location
def getName(file, uuid):
    with open(file) as fd:
        doc = xmltodict.parse(fd.read())
        x = 0
        for x in range(len(doc['VirtualBox']['Global']['MachineRegistry'])):
            for row in doc['VirtualBox']['Global']['MachineRegistry']['MachineEntry']:
                if row['@uuid'] == uuid:
                    # print row['@uuid']+'\t'+row['@src']
                    targetVbox = str(row['@src']).rsplit("""\\""",1)[0]+'\\'
                    # print targetVbox # Prints vbox file name
                    machCfg = find('.vbox', targetVbox)
    with open(machCfg) as fd:
        doc = xmltodict.parse(fd.read())
        name =doc['VirtualBox']['Machine']['@name']
        # print name
        return name


def getSnapDir(file, uuid):
    with open(file) as fd:
        doc = xmltodict.parse(fd.read())
        x = 0
        for x in range(len(doc['VirtualBox']['Global']['MachineRegistry'])):
            for row in doc['VirtualBox']['Global']['MachineRegistry']['MachineEntry']:
                if row['@uuid'] == uuid:
                    # print row['@uuid']+'\t'+row['@src']
                    targetVbox = str(row['@src']).rsplit("""\\""",1)[0]+'\\'
                    # print targetVbox # Prints vbox file name
                    machCfg = find('.vbox', targetVbox)
    with open(machCfg) as fd:
        doc = xmltodict.parse(fd.read())
        snapdir =doc['VirtualBox']['Machine']['@snapshotFolder']
        return snapdir

# Return xml data
def updateSnapDir(file, uuid, newLoc):
    with open(file) as fd:
        doc = xmltodict.parse(fd.read())
        x = 0
        for x in range(len(doc['VirtualBox']['Global']['MachineRegistry'])):
            for row in doc['VirtualBox']['Global']['MachineRegistry']['MachineEntry']:
                if row['@uuid'] == uuid:
                    # print row['@uuid']+'\t'+row['@src']
                    targetVbox = str(row['@src']).rsplit("""\\""",1)[0]+'\\'
                    # print targetVbox # Prints vbox file name
                    machCfg = find('.vbox', targetVbox)
    with open(machCfg) as fd:
        doc = xmltodict.parse(fd.read())
        doc['VirtualBox']['Machine']['@snapshotFolder'] = newLoc
    output = (xmltodict.unparse(doc, pretty=True))
    return output

def find(pattern, path):
    for file in os.listdir(path):
        if file.endswith(pattern):
            # print "Found config file:" + str(file)
            return(os.path.join(path, file))

# getName(vboxConfig,"{4b08775c-2117-4769-9429-d7e6f5859154}")
# print getUUIDS(vboxConfig)
print "Vm\'s in config file"
for each in getUUIDS(vboxConfig):
    print getName(vboxConfig, each) + "\t" + getSnapDir(vboxConfig, each)

# Write new snapshot location
print updateSnapDir(vboxConfig, "{4b08775c-2117-4769-9429-d7e6f5859154}", "This is a new dir")

# updateSrc("""C:\Users\Optiplex 9010\.VirtualBox\VirtualBox2.xml""","{d8f99551-4e5f-43f7-991a-119b046d8013}", """C:\New""")
# outputFile = open("out.xml", "w")
# outputFile.write(output)
# outputFile.close()#