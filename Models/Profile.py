class Profile:

    def __init__(self, profileId='', username='', password=''):
        self.profileId = profileId
        self.username = username

    def getProfileId(self):
        return self.profileId

    def setProfileId(self, profileId):
        self.profileId = profileId
        return self.profileId

    def getUsername(self):
        return self.username

    def setUsername(self, username):
        self.username = username
        return self.username

    def getPassword(self):
        return self.password

    def setPassword(self, password):
        self.password = password
        return self.password