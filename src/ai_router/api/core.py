"""
This module contains the core API functionality for the AI Router application.
"""

from .controllers.prompt_controller import PromptController

def handle_request(prompt):
    new_prompt_controller = PromptController(prompt=prompt)
    category = new_prompt_controller.model.model_classify()

    return {"message": "Request handled successfully", "prompt": prompt, "category": category, "status": 200}