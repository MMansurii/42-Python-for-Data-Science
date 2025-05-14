import time
from datetime import datetime

# Get current timestamp (seconds since January 1, 1970)
current_timestamp = time.time()

# Format with commas (for thousands separator)
formatted_timestamp = f"{current_timestamp:,.4f}"

# Format in scientific notation
scientific_notation = f"{current_timestamp:.2e}"

# Get current date in the format "Oct 21 2022"
current_date = datetime.now().strftime("%b %d %Y")

# Print the results
print(f"Seconds since January 1, 1970: {formatted_timestamp} or {scientific_notation} in scientific notation")
print(f"{current_date}")