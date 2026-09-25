# Main classes of each controller are defined here. Each controller is responsible for handling requests related to its specific domain.
import datetime

class Controller:
    
    def __init__(self, name, description, model, views,  **kwargs):
        self.name = name
        self.description = description
        self.model = model
        self.views = views
        self.created_at = datetime.datetime.now()
        
        self.additional_attributes = kwargs 
        
    def __str__(self):
        return f"Controller(name={self.name}, description={self.description}, created_at={self.created_at}, additional_attributes={self.additional_attributes})"
      
    def __repr__(self):
        return self.__str__()