from git.repo import Repo
import os
import time

commits = 3 # Number of commits you would like to make
TimeBetweenCommits = 1 # Time between each commit in seconds

repo = Repo(os.getcwd())
file = open("file.txt", "a")

def commit():
    file.write('!')
    repo.index.commit('Gotta love commits!')

for i in range(commits-1):
    print(f'Commit {i+1}/{commits}')
    commit()
    time.sleep(TimeBetweenCommits)

file.close()

file = open("file.txt", "w")
file.write('Commits!')
file.close()

repo.index.commit('Gotta love commits!')
print(f'Commit {commits}/{commits}')

print('Pushing...')
origin = repo.remotes[0]
origin.push()
print('Pushed!')

