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

parser = argparse.ArgumentParser(description='Remove entries with given msgid\'s from a .po file.')
parser.add_argument('-p', '--pofile', help='Po file name', required=True)
parser.add_argument('-t', '--target', help='Target filename for processed po file. If not specified, input file will be overwritten')
parser.add_argument('-m', '--msgid', help='msgid to remove', nargs='+')
parser.add_argument('-f', '--msgid-file', help='Path to file with msgid\'s to remove', type=open)
parser.add_argument('-v', '--verbose', help='Display verbose output', action='store_true')
parser.add_argument('--version', action='version', version='%(prog)s 0.1')
args = parser.parse_args()

pofile = polib.pofile(args.pofile)

if (args.target):
    target = args.target
else:
    target = args.pofile

if (args.msgid):
    for msgid in args.msgid:
        remove_msgid(msgid, pofile, args.verbose)

if (args.msgid_file):
    for line in args.msgid_file:
        msgid = line.rstrip('\r\n')
        if (msgid):
            remove_msgid (msgid, pofile, args.verbose)

pofile.save(target)

print target, 'saved.'
