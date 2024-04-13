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

print(days)
for i in range(days):
    CommitsPerDay = random.randint(MinCommits, MaxCommits)
    for x in range(CommitsPerDay):
        subprocess.run(["git", "commit", "--allow-empty", "-m", "Gotta love commits!", "--date", commit_date.isoformat()])
        print(f'Commit {i*x}/{days*CommitsPerDay}')
    commit_date += datetime.timedelta(days=1)

print('Pushing...')
subprocess.run(["git", "push"])
print('Pushed!')

