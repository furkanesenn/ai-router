import json

from .core import Model

# "code", "math", "image", "video", "audio", "long-text", "other"
class PromptModel(Model):
    """A class representing a prompt model with its name, description, and associated controller."""
    PROMPT_SET_FILE_PATH: str = r'C:\Users\furka\Desktop\ai-router\ai-router\src\ai_router\api\models\prompt_set.json'  # Path to the prompt set JSON file
    CATEGORIES: dict[str, str] = {
      "code": "Prompts related to programming, coding, or software development.",
      "math": "Prompts related to mathematical problems, equations, or concepts.",
      "image": "Prompts related to image processing, computer vision, or graphics.",
      "video": "Prompts related to video processing, editing, or analysis.",
      "audio": "Prompts related to audio processing, speech recognition, or music.",
      "long-text": "Prompts that involve generating or analyzing long-form text content.",
    }  # TBT : To be transferred to a separate config file for better maintainability and scalability.

    def __init__(self, name: str, description: str, prompt: str, **kwargs):
        super().__init__(name=name, description=description, **kwargs)
        self.prompt = prompt
        
    def model_classify(self):
        """
        Classifies the prompt into one of the predefined categories using algorithms.
        
        Returns:
            str: The category of the prompt.
        """

        if not self.prompt or not isinstance(self.prompt, str) or self.prompt.strip() == "" or len(self.prompt) < 5:
            raise ValueError("Prompt must be a non-empty string.")

        if len(self.prompt) > 1000:
            raise ValueError("Prompt is too long. Please provide a shorter prompt.")
          
        lowered_prompt = self.prompt.lower()
        
        for category, _ in self.CATEGORIES.items():
            if category in lowered_prompt:
                return category 
              
        # Deep analysis
        prompt_set: dict[str, dict[str, str]] = {} 
        with open(PromptModel.PROMPT_SET_FILE_PATH, 'r') as f:
            prompt_set = json.loads(f.read())

            for category, details in prompt_set.items():
                may_contain = details.get('may-contain', []) 
                must_not_contain = details.get('must-not-contain', [])
                
                if any(word in lowered_prompt for word in must_not_contain):
                    continue  # Skip this category if it contains any must-not-contain words
                if any(word in lowered_prompt for word in may_contain) and not any(word in lowered_prompt for word in must_not_contain):
                    print('Test')
                    return category
                                
                if any(word in lowered_prompt for word in may_contain):
                    return category
            else:
                return "other"  # Default category if no matches found