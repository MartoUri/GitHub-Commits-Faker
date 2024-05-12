import subprocess
import subprocess
import datetime


commit_date_str = "12/01/2023"

commit_date = datetime.datetime.strptime(commit_date_str, "%m/%d/%Y").strftime("%a %b %d %H:%M:%S %Y %z")

subprocess.run(["git", "commit", "--allow-empty", "-m", commit_message, "--date", commit_date])
subprocess.run(["git", "push"])
subprocess.run(["git", "commit", "--allow-empty", "-m", commit_message, "--date", commit_date])
subprocess.run(["git", "push"])
