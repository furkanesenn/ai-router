from .core import Model 

class AIModel(Model): 
  """"A class representing a machine learning model with its name, version, and description."""
  
  def __init__(self, name: str, version: str, description: str ="", endpoint: str = '', token: str = '', **kwargs): 
      super().__init__(name=name, description=description, **kwargs)
      self.version = version
      self.endpoint = endpoint
      self.token = token
        
  def __repr__(self):
    return f"Model(name={self.name}, version={self.version}, description={self.description})"
  
  def __str__(self):
    return f"{self.name} v{self.version}: {self.description}"
  
  def use(self):
    return f"Using model {self.name} version {self.version}"