from email.headerregistry import Address
import webbrowser
import sys

if len(sys.argv) > 1:
    # Get addres from command line.
    address = " ".join(sys.argv[1:])
