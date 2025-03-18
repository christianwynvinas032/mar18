class GraphicDesigner:
    def designLogo(self):
        print("Designing the logo for the brand.")

class WebDeveloper:
    def buildWebsite(self):
        print("Building the website for the brand.")

class DigitalSolutionsProvider(GraphicDesigner, WebDeveloper):
    def deliverProject(self):
        print("Delivering the project:")
        self.designLogo()  
        self.buildWebsite()

digital_solution_provider = DigitalSolutionsProvider()
digital_solution_provider.deliverProject()
