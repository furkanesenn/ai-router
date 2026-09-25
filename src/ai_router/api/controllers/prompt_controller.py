

from ai_router.api.models.prompt_model import PromptModel

from .core import Controller


class PromptController(Controller):
    def __init__(self, prompt):
        super().__init__(
            name="Prompt Controller",
            description="Categorizes prompts into specific domains",
            model=PromptModel(name="Prompt Model", description="A model for classifying prompts", prompt=prompt),
            views=[], 
            prompt=prompt
        )