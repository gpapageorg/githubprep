from github import Github
from github import Auth
import sys

TOKEN_FILENAME = "token"
COMMANDS = ["createRepo","deleteRepo"]

argc = len(sys.argv)
argv = sys.argv[1:]

class PrepareGithub:
    def __init__(self, token):

        self.auth = Auth.Token(self.readToken(token))
        self.g = Github(auth = self.auth)
        
        self.user = self.g.get_user()

      #  for repo in self.user.get_repos():
       #     print(repo.name)

    def createRepo(self, repoName):
        repo = self.user.create_repo(repoName)

    def deleteRepo(self, repoName):
        repo = self.user.get_repo(repoName)
        repo.delete()

    def readToken(self, filename):
        f = open(filename, "r")
        token = f.read().replace("\n", '')
        f.close()
        return token

    def __del__(self):
        self.g.close()    


def checkArgs():
    if (argc != 3):
        print("Error Wrong Arguments")
        exit()

    if argv[0] not in COMMANDS:
        print("Wrong Command Available Commands:", end = " ")
        for command in COMMANDS:
            print(command, end = " ")
        print()
        exit()

def executeCommand(i):
    if argv[0] == COMMANDS[0]: ### CREATE REPO ###
        try:
            i.createRepo(argv[1])
            print("Repository Created With Name:", argv[1])
        except:
            print("Error While Creating")

    elif argv[0] == COMMANDS[1]: ### DELETE REPO ###
        try:
            i.deleteRepo(argv[1])
            print("Repository Named", argv[1], "Deleted")
        except:
            print("Error While Deleting")




def main():
    checkArgs() ### CHECKING GIVEN ARGUMENTS ###
    instance = PrepareGithub(TOKEN_FILENAME) ### CREATING MAIN GITHUB INSTANCE ###
    executeCommand(instance) ### EXECUTING GIVEN COMMAND ###



if __name__ == "__main__":
    main()
