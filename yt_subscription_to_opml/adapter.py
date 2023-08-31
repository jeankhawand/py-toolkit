import csv
# export it from https://takeout.google.com/takeout/custom/youtube
csv_filename = 'subscriptions.csv'
xml_filename = 'feed.opml'

xml_template = '''
<outline title="{title}" text="{title}" xmlUrl="https://www.youtube.com/feeds/videos.xml?channel_id={id}" htmlUrl="{url}"></outline>
'''

with open(csv_filename, 'r') as csv_file, open(xml_filename, 'w') as xml_file:
    csv_reader = csv.DictReader(csv_file)
    
    xml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    xml_file.write('<opml version="2.0">\n')
    
    for row in csv_reader:
        channel_id = row['Channel Id']
        channel_url = row['Channel Url']
        channel_title = row['Channel Title']
        
        xml_entry = xml_template.format(id=channel_id, url=channel_url, title=channel_title)
        xml_file.write(xml_entry)
    
    xml_file.write('</opml>\n')

print(f'XML file "{xml_filename}" has been generated.')
