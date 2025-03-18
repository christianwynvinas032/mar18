class CreativeEntrepreneur:
    def __init__(self, trending_topic):
        self.trending_topic = trending_topic

    def brainstormIdeas(self):
        print("Brainstorming creative ideas for content.")

class RawDesigner(CreativeEntrepreneur):
    def createDesign(self):
        print("Creating raw and unique designs for content.")

class ContentStrategist(CreativeEntrepreneur):
    def planContent(self):
        print("Planning content strategy to engage audience.")

class TalesFromTheIslandsCreator(RawDesigner, ContentStrategist):
    def produceReel(self):
        print("Producing a content reel based on current trends...")
        if self.trending_topic == "conspiracy theories":
            print("Focusing on creating a reel about conspiracy theories.")
        elif self.trending_topic == "motivational stories":
            print("Focusing on creating a reel about motivational stories.")
        else:
            print("Focusing on content without a clear trending topic.")

creator = TalesFromTheIslandsCreator(trending_topic="motivational stories")
creator.brainstormIdeas()
creator.createDesign()
