import re

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

# 1.
# Event: Workshop & Tutorial proposals due
# Date: November 21, 2019

# 2.
# Event: Notification of acceptance
# Date: December 1, 2019

text_pattern = re.compile(r'(.*?):')
all_text = text_pattern.findall(text)
print(all_text)

date_pattern = re.compile(r'\w+\s+\d+,\s\d{4}')
all_dates = date_pattern.findall(text)
print(all_dates)

for event, date in zip(all_text, all_dates):
    print(f'Event: {event}')
    print(f'Date: {date}\n')
