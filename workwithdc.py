import winrm
#hi
class workwithdc():#
    def __init__(self):
        self.host = '4.227.226.102'
        self.domain = 'yourmom.dom'
        self.user = 'guym'
        self.password = 'A123a123'
        self.session = winrm.Session(self.host, auth=('{}@{}'.format(self.user,self.domain),self.password), transport='ntlm')


    def unlockAccount(self, username):
        result = self.session.run_ps(f"C:\\Chatbot\\Scripts\\UnlockUser.ps1 {username}") # To run Powershell block
        #print(result)
        print(result.std_out.decode())
        return result

    def checkPerms(self,url):
        result = self.session.run_ps(f'C:\\Chatbot\\Scripts\\CheckFolderAccessWithCurrentUser.ps1 {url}')
        print(result)
        return result
    
    def checkPing(self,computer):
        result = self.session.run_ps(f'C:\\Chatbot\\Scripts\\PingWorkstation.ps1 {computer}')
        print(result)
        return result
    
    def fixSlayer(self,computer):
        result = self.session.run_ps(f'C:\\Chatbot\\Scripts\\FixOutlookSlayer.ps1 {computer}')
        print(result)
        return result