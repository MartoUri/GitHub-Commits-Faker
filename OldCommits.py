import subprocess
import subprocess
import datetime
import random

CommitsFrom = "12/01/2023" #Make sure to put in in date format MM/DD/YYYY
MaxCommits = 25 #Max commits per day
MinCommits = 5 #Min commits per day

today = datetime.datetime.now().strftime("%m/%d/%Y")
commit_date = datetime.datetime.fromisocalendar(int(today.split('/')[2]), 1, 1)
days = (datetime.datetime.now() - datetime.datetime.strptime(CommitsFrom, "%m/%d/%Y")).days

CommitsPerDay = [random.randint(MinCommits, MaxCommits) for _ in range(days)]
SumCommits = sum(CommitsPerDay)

file = open('commits.txt', 'a')

print(days)
for i in range(days):
    CommitsUntilNow = sum(CommitsPerDay[:i])
    for x in range(CommitsPerDay[i]):
        file.write("!")
        subprocess.run(["git", "commit", "--allow-empty", "-m", "Gotta love commits!", "--date", commit_date.isoformat()])
        print(f'Commit {CommitsUntilNow + x}/{SumCommits}   ---   {(CommitsUntilNow+x)/SumCommits*100:.2f}% done')
    commit_date += datetime.timedelta(days=1)

file.close()
file.open('commits.txt', 'w')
file.write("Commits!")
file.close()

print('Pushing...')
#subprocess.run(["git", "push"])
print('Pushed!')

