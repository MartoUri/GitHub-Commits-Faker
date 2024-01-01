import subprocess
import subprocess
import datetime
import random

CommitsFrom = "12/01/2022" #Make sure to put in in date format MM/DD/YYYY
MaxCommits = 20 #Max commits per day
MinCommits = 5 #Min commits per day

today = datetime.datetime.now().strftime("%m/%d/%Y")
commit_date = datetime.datetime.fromisocalendar(int(today.split('/')[2]), 1, 1)
days = (datetime.datetime.now() - datetime.datetime.strptime(CommitsFrom, "%m/%d/%Y")).days

CommitsPerDay = [random.randint(MinCommits, MaxCommits) for _ in range(days)]
SumCommits = sum(CommitsPerDay)

print(days)
for i in range(days):
    CommitsUntilNow = sum(CommitsPerDay[:i])
    for x in range(CommitsPerDay[i]):
        subprocess.run(["git", "commit", "--allow-empty", "-m", "Gotta love commits!", "--date", commit_date.isoformat()])
        print(f'Commit {CommitsUntilNow + x}/{SumCommits}')
    commit_date += datetime.timedelta(days=1)

print('Pushing...')
subprocess.run(["git", "push"])
print('Pushed!')

