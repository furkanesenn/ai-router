
class Model:
    def __init__(self, name, description, **kwargs):
        self.name = name
        self.description = description
        self.additional_attributes = kwargs  # Store any additional attributes passed in

    def __str__(self):
        return f"{self.name}: {self.description}"

    def __repr__(self):
        return f"Model(name={self.name}, description={self.description}, additional_attributes={self.additional_attributes})"