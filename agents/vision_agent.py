import json
from pathlib import Path

import torch
from PIL import Image
from rapidfuzz import fuzz
from transformers import (
    BlipProcessor,
    BlipForConditionalGeneration,
)

processor = None
model = None


def load_model():
    global processor, model

    if processor is None:
        print("Loading BLIP model...")

        processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

        model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

        model.eval()

        print("BLIP model loaded successfully!")


def load_food_keywords():
    path = Path(__file__).parent.parent / "data" / "food_keywords.json"

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_caption(image):
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
            max_new_tokens=20,
            num_beams=5,
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


def extract_foods(caption):
    keywords = load_food_keywords()

    detected = []

    # Exact match
    for food in keywords:
        if food.lower() in caption:
            detected.append(food)

    # Fuzzy fallback
    if not detected:
        for food in keywords:
            score = fuzz.partial_ratio(food.lower(), caption)

            if score >= 90:
                print(f"FUZZY MATCH -> {food} ({score:.1f})")
                detected.append(food)

    return list(dict.fromkeys(detected))


def detect_food(image):

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