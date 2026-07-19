"""
Vision Agent for NourishBot.

Responsible for:
- Loading the BLIP image captioning model
- Generating image captions
- Extracting food keywords from captions
"""

import json
from pathlib import Path
from typing import Any

import torch
from PIL import Image
from rapidfuzz import fuzz
from transformers import (
    BlipForConditionalGeneration,
    BlipProcessor,
)

# ==========================================================
# Configuration
# ==========================================================

MODEL_NAME = "Salesforce/blip-image-captioning-base"

MAX_NEW_TOKENS = 20
NUM_BEAMS = 5
FUZZY_THRESHOLD = 90

# ==========================================================
# Global Model Cache
# ==========================================================

processor: BlipProcessor | None = None
model: BlipForConditionalGeneration | None = None
_food_keywords: list[str] | None = None


# ==========================================================
# Model Loading
# ==========================================================

def load_model() -> None:
    """
    Load the BLIP model only once.
    """

    global processor, model

    if processor is not None and model is not None:
        return

    print("Loading BLIP model...")

    processor = BlipProcessor.from_pretrained(MODEL_NAME)

    model = BlipForConditionalGeneration.from_pretrained(MODEL_NAME)

    model.eval()

    print("BLIP model loaded successfully!")


# ==========================================================
# Food Keyword Loading
# ==========================================================

def load_food_keywords() -> list[str]:
    """
    Load food keywords from JSON.

    The keywords are cached after the first load.
    """

    global _food_keywords

    if _food_keywords is not None:
        return _food_keywords

    path = Path(__file__).parent.parent / "data" / "food_keywords.json"

    with open(path, "r", encoding="utf-8") as file:
        _food_keywords = json.load(file)

    return _food_keywords


# ==========================================================
# Caption Generation
# ==========================================================

def generate_caption(image: Image.Image | Any) -> str:
    """
    Generate an image caption using BLIP.

    Args:
        image: PIL Image or NumPy array.

    Returns:
        Generated caption.
    """

    load_model()

    if not isinstance(image, Image.Image):
        image = Image.fromarray(image)

    image = image.convert("RGB")

    inputs = processor(
        images=image,
        return_tensors="pt",
    )

    with torch.no_grad():
        output = model.generate(
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            num_beams=NUM_BEAMS,
            repetition_penalty=2.0,
            no_repeat_ngram_size=2,
            early_stopping=True,
        )

    caption = processor.decode(
        output[0],
        skip_special_tokens=True,
    ).lower()

    print("\n=== AI CAPTION ===")
    print(caption)

    return caption


# ==========================================================
# Food Extraction
# ==========================================================

def extract_foods(caption: str) -> list[str]:
    """
    Extract food names from a generated caption.

    Performs:
    1. Exact keyword matching
    2. Fuzzy matching fallback
    """

    keywords = load_food_keywords()

    detected: list[str] = []

    # Exact Match
    for food in keywords:
        if food.lower() in caption:
            detected.append(food)

    # Fuzzy Match
    if not detected:
        for food in keywords:
            score = fuzz.partial_ratio(food.lower(), caption)

            if score >= FUZZY_THRESHOLD:
                print(f"FUZZY MATCH -> {food} ({score:.1f})")
                detected.append(food)

    # Remove duplicates while preserving order
    return list(dict.fromkeys(detected))


# ==========================================================
# Main Detection Pipeline
# ==========================================================

def detect_food(image: Image.Image | Any) -> dict[str, Any]:
    """
    Detect foods from an image.

    Args:
        image: Uploaded image.

    Returns:
        Dictionary containing:
            caption : Generated BLIP caption
            foods   : List of detected foods
    """

    if image is None:
        return {
            "caption": "",
            "foods": [],
        }

    caption = generate_caption(image)

    foods = extract_foods(caption)

    print("\n=== DETECTED FOODS ===")
    print(foods)

    return {
        "caption": caption,
        "foods": foods,
    }