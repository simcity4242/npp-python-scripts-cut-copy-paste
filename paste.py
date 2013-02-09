# Get left anchor position from current selection
sel_start = editor.getSelectionStart()

# Retrieve position of start of line where left anchor is
editor.setCurrentPos(sel_start)
editor.home()
start = editor.getCurrentPos()

# Unselect all lines and set caret to start of line where left anchor was
editor.setSelectionStart(start)
editor.setSelectionEnd(start)
editor.setCurrentPos(start)

# Paste text coming from clipboard
editor.paste()
