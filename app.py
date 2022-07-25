import dropbox
class Transferdata:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    access_token = 'sl.BMEiClRDAqi9nHtXHPkj9avd6yQ9kafLYz7XUUxVeVRfVYSiefo_7762IJdVHdejhIMh-etzJ-FXSZMvvib8A7_mf38KrZOAXphdXGwE4JBhDSd8lOMk9gRI1sSlb9r8PA-HMspevKZ7'
    transferdata = Transferdata(access_token)

    file_from = input("enterfile")
    file_to = input("enterfullpath")
    transferdata.upload_file(file_from,file_to)
    print("file moved")
main()