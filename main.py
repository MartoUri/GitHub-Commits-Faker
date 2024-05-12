from git.repo import Repo
import os
repo = Repo(os.getcwd())
file = open("file.txt", "r+")
def commit():
    file.write('!')
    repo.index.commit('Gotta love commits!')
    origin = repo.remotes[0]
    origin.push()
commit()
file.close()
