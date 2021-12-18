# "C:\Users\op6\AppData\Roaming\Notepad++\plugins\config\PythonScript\scripts\OpOpenFile.py"

#console.show()
#console.clear()

print "Start OpOpenFile -------------------------------"

import subprocess

selsCt = editor.getSelections() # immer 1
#selsCt = 0
print "selsCt:", selsCt
if selsCt == 1:
    sPos = editor.getSelectionNStart(0)
    ePos = editor.getSelectionNEnd(0)
    print "sPos:", sPos, "ePos:", ePos
    if sPos != ePos:
        sWrd = editor.getTextRange(sPos, ePos)
        print "Selected Word:", sWrd
        # open with default
        #subprocess.call(sWrd)
        mbox = notepad.messageBox("Open: '" + sWrd + "'", "OpOpenFile - Python", MESSAGEBOXFLAGS.YESNOCANCEL + MESSAGEBOXFLAGS.DEFBUTTON1 + MESSAGEBOXFLAGS.ICONQUESTION)
        print mbox  # YES=6 NO=7 CANCEL=2
        if mbox == 6:    # MESSAGEBOXFLAGS.RESULTOK
            print "subprocess.Popen..."
            p = subprocess.Popen(args = sWrd, shell = True)
            print p
    else:
        print "sPos == ePos !"
else:
    print("No Selection !")
    notepad.messageBox("No Selection !", "OpOpenFile - Python", MESSAGEBOXFLAGS.ICONSTOP)

################################
# https://community.notepad-plus-plus.org/topic/18997/i-would-like-to-have-a-notepad-shortcut-that-will-jump-to-a-line-in-a-file/2
#from Npp import editor, SCINTILLANOTIFICATION
#
#def goto(args):
#    start = editor.wordStartPosition(args['position'], False)
#    end = editor.getLineEndPosition(editor.lineFromPosition(args['position']))
#    print(editor.getTextRange(start, end))        
#
#editor.callback(goto, [SCINTILLANOTIFICATION.HOTSPOTCLICK])
###############################

print "End OpOpenFile."
# ende #
