import os, sys, time
import xml.etree.ElementTree as ET

def menu():
	print "----------------------------------------------"
	print "\t ISOAPPLET CAP FILE GENERATOR"
	print "\t\t by @Luis-3M"
	print "----------------------------------------------"
	return

def getPackages():
	os.system('curl -L https://www.dropbox.com/s/wbj963ya1shpvg2/javacard_2.2.2.tar.gz?dl=1 -O -J')
	os.system('tar -xf javacard_2.2.2.tar.gz')
	os.system('rm -rf javacard_2.2.2.tar.gz')
	os.system('git clone https://github.com/philipWendland/IsoApplet.git')
	return

def buildCAP():
	os.chdir(os.path.expanduser('IsoApplet'))
	os.system('git submodule init && git submodule update')
	xmlParse()
	os.system('ant')
	os.system('mv IsoApplet.cap ~/')
	os.chdir(os.path.expanduser('~'))
	os.system('rm -rf IsoApplet/ Source/')
	print
	print '\033[92m'+str(os.path.abspath('IsoApplet.cap'))+'\033[0m'
	return

def xmlParse():
	homePath = str(os.path.expanduser('~'))
	tree = ET.parse('build.xml')
	root = tree.getroot()
	for javacard in root.iter('javacard'):
		javacard.set('jckit', homePath+'/Source/javacard/javacard_2_2_2')
	for cap in root.iter('cap'):
                cap.set('jckit', homePath+'/Source/javacard/javacard_2_2_2')
	tree.write('build.xml')
	return

def main():
	start = time.time()
	os.system('clear')
	os.chdir(os.path.expanduser('~'))
	menu()
	try:
		opt = raw_input("Do you have '\033[4m'ANT'\033[0m' and '\033[4m'GIT'\033[0m' installed? ")
		if opt.lower() == "yes" or opt.lower() == "y":
			getPackages()
			buildCAP()
			print
		elif opt.lower() == "no" or opt.lower() == "n":
			print "Please install them first.."
		else:
			print "Really? Don't even think about it.. Yes or No mate."
	except KeyboardInterrupt:
		sys.exit(0)
	print
	end = time.time()
	execTime = round(end-start,4)
	
	print "Program executed in "+str(execTime)+" seconds"
	return

if __name__ == "__main__":
	main()
