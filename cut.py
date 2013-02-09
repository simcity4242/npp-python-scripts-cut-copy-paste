# Get anchors position from current selection
sel_start = editor.getSelectionStart()
sel_end = editor.getSelectionEnd()

# Retrieve position of start of line where left anchor is
editor.setCurrentPos(sel_start)
editor.home()
start = editor.getCurrentPos()

# Retrieve position of start of line under where right anchor is to cut complete line (characters + EOL)
editor.setCurrentPos(sel_end)
editor.home()
editor.lineDown()
end = editor.getCurrentPos()

# Select all lines and cut it to clipboard
editor.setSelectionStart(start)
editor.setSelectionEnd(end)
editor.cut()

# Replace anchors and caret at start of line from where we cut lines
editor.setSelectionStart(start)
editor.setSelectionEnd(start)
editor.setCurrentPos(start)