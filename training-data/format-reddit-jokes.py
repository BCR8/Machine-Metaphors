# Read json file in as a string
with open('reddit_jokes_unformatted.json', 'r') as file:
	orig_file_text = file.read()

# Covert json to an object we can use
import json
obj = json.loads(orig_file_text)

# Format lines appropriately for our purpose
# Careful - will append if file already exists
output_file = open("reddit_jokes_formatted.txt", "ab")
for current_element in obj:
	# Combine title and body
	temp_line = current_element['title']
	temp_line += ' '
	temp_line += current_element['body']
	# Remove newlines
	temp_line = temp_line.replace("\r","")
	temp_line = temp_line.replace("\n","")
	# Write to file in UTF-8
	output_file.write(temp_line.encode('utf8'))
	output_file.write('\n'.encode('utf8'))
output_file.close()
