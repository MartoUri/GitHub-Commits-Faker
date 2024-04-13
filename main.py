import subprocess
import datetime
import time

commits = 3 # Number of commits you would like to make
TimeBetweenCommits = 1 # Time between each commit in seconds


def commit():

    today = datetime.datetime.now().strftime("%m/%d/%Y")

    subprocess.run(["git", "commit", "--allow-empty", "-m", "Gotta love commits!", "--date", today])

for i in range(commits):
    print(f'Commit {i+1}/{commits}')
    commit()
    time.sleep(TimeBetweenCommits)

print('Pushing...')
subprocess.run(["git", "push"])
print('Pushed!')

