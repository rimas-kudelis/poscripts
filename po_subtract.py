import argparse
import polib

def remove_msgid(msgid, pofile, verbose):
    entry = pofile.find(msgid)
    if (entry):
        if (verbose):
            print 'Removing entry:', msgid
        pofile.remove(entry)
    else:
        if (verbose):
            print 'Entry not found:', msgid

parser = argparse.ArgumentParser(description='Remove entries from a .po file which are defined in another .po file.')
parser.add_argument('-p', '--pofile', help='Name of the po file to subtract entries from', required=True)
parser.add_argument('-r', '--remove-file', help='Name of the po file with strings to subtract from -p', required=True)
parser.add_argument('-t', '--target', help='Target filename for processed po file. If not specified, input file specified with -p will be overwritten')
parser.add_argument('-v', '--verbose', help='Display verbose output', action='store_true')
parser.add_argument('--version', action='version', version='%(prog)s 0.1')
args = parser.parse_args()

pofile = polib.pofile(args.pofile)
removefile = polib.pofile(args.remove_file)

if (args.target):
    target = args.target
else:
    target = args.pofile

for entry in removefile:
    if (entry.msgid != ''):
        remove_msgid(entry.msgid, pofile, args.verbose)

pofile.save(target)

print target, 'saved.'
