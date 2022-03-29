import argparse
import logging as log
from .reader import LISEreader
from .version import __version__

def main():
    scriptname = 'lisereader' 
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, default='test/E143_TEline-ESR-72Ge.lpp', help='Name of the LISE file to read.')
    parser.add_argument('-n', '--nuclei', type=str, nargs='?',
                        help='Nuclei name to get its info.')
    
    parser.add_argument('-i', '--ian',
                        help='Get info for all the nuclei in the LISE file', action='store_true')
    parser.add_argument('-v', '--verbose',
                        help='Increase output verbosity', action='store_true')
    

    args = parser.parse_args()
    
    print(f'Running {scriptname} V{__version__}')
    if args.verbose: log.basicConfig(level=log.DEBUG)

    # here we go:
    log.info(f'File {args.filename} passed for reading')
    
    lisedata=LISEreader(args.filename)
    print(lisedata.data)
    if args.nuclei: print(lisedata.get_info(args.nuclei))
    if args.ian: print(lisedata.get_info_all())

if __name__ == '__main__':
    main()
