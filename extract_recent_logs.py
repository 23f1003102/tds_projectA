import os
import glob

# Path to logs directory
log_dir = "/data/logs/"

# Find all .log files in the directory
log_files = glob.glob(os.path.join(log_dir, "*.log"))

# Sort log files by modification time (newest first)
log_files.sort(key=os.path.getmtime, reverse=True)

# Take the 10 most recent log files
recent_logs = log_files[:10]

# Extract the first line from each file
first_lines = []
for log_file in recent_logs:
    try:
        with open(log_file, "r") as f:
            first_line = f.readline().strip()  # Read first line
            first_lines.append(first_line)
    except Exception as e:
        print(f"Error reading {log_file}: {e}")

# Write the first lines to the output file
output_file = "/data/logs-recent.txt"
with open(output_file, "w") as f:
    f.write("\n".join(first_lines))

print(f"Extracted first lines saved to {output_file}")
