from github import Github
from github import Auth
import sys, os

TOKEN_FILENAME = "token"
COMMANDS = ["createRepo","deleteRepo", "defaultRoutine", "listRepos"]
MAXARGS = 3 ### MAXIMUM ARGUMENT NUMBER ###

argc = len(sys.argv)
argv = sys.argv[1:]

##################### --- CLASS SECTION ##########################
class PrepareGithub:
    def __init__(self, token):

        self.auth = Auth.Token(self.readToken(token))
        self.g = Github(auth = self.auth)
        
        self.user = self.g.get_user()


    def createRepo(self, repoName):
        repo = self.user.create_repo(repoName)

    def deleteRepo(self, repoName):
        repo = self.user.get_repo(repoName)
        repo.delete()

    def listRepos(self):
      for repo in self.user.get_repos():
        print(repo.name)

    def readToken(self, filename):
        f = open(filename, "r")
        token = f.read().replace("\n", '')
        f.close()
        return token

    def __del__(self):
        self.g.close()    

#################### --- FUNCTIONS SECTION --- ####################
def initializeGit():
    print("Writing Default README...\n")
    os.system('''echo "# ''' + argv[1] + '''" >> README.md''')
    print("Initializing Git...\n\n")
    os.system("git init")
    os.system("git add README.md")
    os.system('''git commit -m "Initial Commit " ''')
    os.system("git branch -M main")
    os.system("git branch developMain")
    os.system("git remote add origin git@github.com:gpapageorg/" + argv[1] + ".git")
    os.system("git push -u origin main")


def checkArgs():
    if argc > MAXARGS:
        print("Wrong Argument Number")
        exit()

    if argv[0] not in COMMANDS:
        print("Wrong Command Available Commands:", end = " ")
        for command in COMMANDS:
            print(command, end = " ")
        print()
        exit()

def executeCommand(i):
    if argv[0] == COMMANDS[0] and argc == 3: ### CREATE REPO ###
        try:
            i.createRepo(argv[1])
            print("Repository Created With Name:", argv[1])
        except:
            print("Error While Creating")
            exit()

    elif argv[0] == COMMANDS[1] and argc == 3: ### DELETE REPO ###
        try:
            i.deleteRepo(argv[1])
            print("Repository Named", argv[1], "Deleted")
        except:
            print("Error While Deleting")
            exit()

    elif argv[0] == COMMANDS[2] and argc == 3:
        ''' ### EXECUTING DEFAULT ROUTINE 
                1) INITIALIZING GIT
                2) CREATING GITHUB REPOSITORY
        '''
        try:
            i.createRepo(argv[1])
            initializeGit()
        except:
            print("Error While Executing Default Routine")
            exit()

    elif argv[0] == COMMANDS[3] and argc == 2:
        try:
            i.listRepos()
        except:
            print("Error While Listing Repos")
            exit()

    else:
        print("Error In Executing Command")
        exit()
        




############ --- MAIN FUNCTION EXECUTED WHEN RUN --- ##############
def main():
    checkArgs() ### CHECKING GIVEN ARGUMENTS ###
    instance = PrepareGithub(TOKEN_FILENAME) ### CREATING MAIN GITHUB INSTANCE ###
    executeCommand(instance) ### EXECUTING GIVEN COMMAND ###



if __name__ == "__main__":
    main()
