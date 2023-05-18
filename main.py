import feedparser
import csv
from datetime import datetime

# Azure updates RSS feed URL
url = "https://azure.microsoft.com/en/updates/feed"

# Parse the feed
feed = feedparser.parse(url)

# Initialize a list to store entries
entries = []

# Get the current month and the previous month
current_month = datetime.now().month
previous_month = current_month - 1 if current_month != 1 else 12

# Loop through the feed entries
for entry in feed.entries:
    # Convert published date to yyyymmdd format
    published_date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
    formatted_published_date = published_date.strftime("%Y%m%d")

    # Skip the entry if the published month is not the current month or the previous month
    if published_date.month not in [current_month, previous_month]:
        continue

    # Determine the status based on the title
    title_lower = entry.title.lower()
    if title_lower.startswith('preview'):
        status = 'Preview'
    elif title_lower.startswith('public preview'):
        status = 'Public Preview'
    elif title_lower.startswith('generally available') or title_lower.startswith('general availability'):
        status = 'GA'
    elif title_lower.startswith('private preview'):
        status = 'Private Preview'
    elif title_lower.startswith('ga'):
        status = 'GA'
    else:
        status = 'N/A'

    # Check if status is N/A and 'retired' is in the summary, then set status to 'Retirements'
    summary_lower = entry.summary.lower()
    if status == 'N/A' and 'retired' in summary_lower:
        status = 'Retirements'

    entries.append({
        'Status': status,
        'Title': entry.title,
        'Link': entry.link,
        'Published': formatted_published_date,
        'Summary': entry.summary,
        'Content': entry.content[0].value if 'content' in entry else 'N/A'
    })

# Define the CSV file name based on the current date
csv_file_name = f"azure_updates_{datetime.now().strftime('%Y%m%d')}.csv"

# Write the entries to the CSV file
with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=entries[0].keys())
    writer.writeheader()
    writer.writerows(entries)

print(f"This month and last month's updates are written to {csv_file_name}")
print(f"Data written to {csv_file_name}")
