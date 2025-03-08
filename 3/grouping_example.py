import re
'''
2024-01-01

(\d{4})-(\d{2})-({\d}) .split('-')
'''

pattern = r'(\d{4})-(\d{2})-(\d{2})'
text = "This event occurred on 2024-01-01, 2023-12-31"
for date in re.findall(pattern, text):
    print(date[0], date[1])

pattern = r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})'
text = "This event occurred on 2024-01-01, 2023-12-31"
for date in re.finditer(pattern, text):
    print(date.groupdict())
