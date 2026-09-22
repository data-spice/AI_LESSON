import subprocess
import time
from pathlib import Path
from datetime import datetime

FILE = Path("activity.txt")
NUMBER_OF_COMMITS = 20


def run(command):
    result = subprocess.run(
        command,
        shell=True,
        text=True,
        capture_output=True
    )

    if result.returncode != 0:
        print(result.stderr)
        raise SystemExit(1)

    return result.stdout.strip()


# Create the file
FILE.touch()

for i in range(1, NUMBER_OF_COMMITS + 1):

    # Add something new to the file
    with FILE.open("a") as f:
        f.write(
            f"Commit {i} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

    # Stage the file
    run(f'git add "{FILE}"')

    # Commit
    commit_message = f"Update activity file #{i}"
    run(f'git commit -m "{commit_message}"')

    print(f"Created commit {i}/{NUMBER_OF_COMMITS}")

    # Small delay
    time.sleep(1)

print("\nDone!")