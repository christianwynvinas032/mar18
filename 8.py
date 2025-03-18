ContentCreator:
    def __init__(self, name, followers):
        self.name = name
        self.followers = followers 

    def createPost(self):
        if self.followers > 1000:
            print(f"{self.name} is creating a trending post!")
        else:
            print(f"{self.name} is creating a post for a smaller audience.")


class Tiktoker(ContentCreator):
    def __init__(self, name, followers, tiktok_handle):
        super().__init__(name, followers)
        self.tiktok_handle = tiktok_handle

    def recordVideo(self):
        print(f"{self.name} is recording a TikTok video at {self.tiktok_handle}")


tiktoker = Tiktoker("yin", 20 000, "@yinoffical")
tiktoker.createPost()
tiktoker.recordVideo()



