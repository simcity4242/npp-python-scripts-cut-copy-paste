# Get first and last line selected
first_line = editor.lineFromPosition(editor.getSelectionStart())
last_line = editor.lineFromPosition(editor.getSelectionEnd())

# Copy all lines selected
text = ""
for i in range(first_line, last_line + 1):
	text += editor.getLine(i)
	
# Write lines in clipboard
editor.copyText(text)
