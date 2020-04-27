# Note_Recovery
Small post-processor for ydkhatri's mac_apt NOTES plugin. takes CSV input and outputs a collection of html files that can be imported into the Notes app.

# Usage
Run like any python3 program. Takes three arguments:
- path to input file
- path to output directory (must exist already)
- Input file's encoding

*example:* `python3 NoteRecover.py /Users/username/Documents/Input.csv /Users/username/Desktop/OutputDir/ "utf-16le"`

# Special thanks
Massive thanks to [ydkhatri](https://github.com/ydkhatri/) for doing the really hard work making the incredible [mac_apt](https://github.com/ydkhatri/mac_apt)
