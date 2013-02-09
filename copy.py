# Get anchors and caret position from current selection
caret_pos = editor.getCurrentPos()
sel_start = editor.getSelectionStart()
sel_end = editor.getSelectionEnd()

# Retrieve position of start of line where left anchor is
editor.setCurrentPos(sel_start)
editor.home()
start = editor.getCurrentPos()

# Retrieve position of start of line under where right anchor is to copy complete line (characters + EOL)
editor.setCurrentPos(sel_end)
editor.home()
editor.lineDown()
end = editor.getCurrentPos()

# Select all lines and copy it to clipboard
editor.setSelectionStart(start)
editor.setSelectionEnd(end)
editor.copy()

# Replace anchors and caret at original position
editor.setSelectionStart(sel_start)
editor.setSelectionEnd(sel_end)
editor.setCurrentPos(caret_pos)