# Retrieve position of start of line where left anchor is
editor.setCurrentPos(editor.getSelectionStart())
editor.home()

# Unselect all lines and set caret to start of line where left anchor was
editor.setSelectionStart(editor.getCurrentPos())
editor.setSelectionEnd(editor.getCurrentPos())
editor.setCurrentPos(editor.getCurrentPos())

# Paste text coming from clipboard
editor.paste()
