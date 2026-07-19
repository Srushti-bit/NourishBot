"""
NourishBot Application.

Provides a Gradio interface for:
- Food image analysis
- Nutrition reporting
- Healthy recipe generation
"""

import gradio as gr
from PIL import Image

from agents.analysis_agent import analyze_meal
from agents.recipe_agent import generate_recipe
from agents.vision_agent import detect_food

APP_TITLE = "🥗 NourishBot"


def process_food(
    image: Image.Image | None,
    diet: str,
    workflow: str,
) -> str:
    """
    Process an uploaded food image.

    Args:
        image: Uploaded PIL image.
        diet: Selected diet preference.
        workflow: Analysis or Recipe.

    Returns:
        Formatted application response.
    """

    if image is None:
        return "❌ Please upload a food image."

    try:
        vision_result = detect_food(image)

        caption = vision_result["caption"]
        detected_foods = vision_result["foods"]

        if not detected_foods:
            return (
                "=============================\n"
                "🤖 AI CAPTION\n"
                "=============================\n\n"
                f"{caption}\n\n"
                "❌ No known food items were detected.\n\n"
                "Try:\n"
                "• A clearer image\n"
                "• A closer view of the meal\n"
                "• Better lighting"
            )

        if workflow == "Analysis":
            result = analyze_meal(detected_foods)

        elif workflow == "Recipe":
            result = generate_recipe(
                detected_foods,
                diet,
            )

        else:
            return "Invalid workflow selected."

        return (
            "=============================\n"
            "🤖 AI CAPTION\n"
            "=============================\n\n"
            f"{caption}\n\n"
            "=============================\n"
            "🍽️ DETECTED FOODS\n"
            "=============================\n\n"
            f"{', '.join(detected_foods)}\n\n"
            f"{result}"
        )

    except Exception as exc:
        return (
            "An unexpected error occurred.\n\n"
            f"{type(exc).__name__}: {exc}"
        )


def build_interface() -> gr.Blocks:
    """
    Build the Gradio interface.
    """

    with gr.Blocks(title=APP_TITLE) as app:

        gr.Markdown(f"# {APP_TITLE}")

        gr.Markdown(
            "Upload a food image to receive AI-powered "
            "nutrition analysis or healthy recipe suggestions."
        )

        image_input = gr.Image(
            type="pil",
            label="📷 Upload Food Image",
        )

        diet = gr.Dropdown(
            choices=[
                "None",
                "Vegan",
                "Vegetarian",
                "Gluten-Free",
                "Keto",
            ],
            value="None",
            label="🥦 Diet Preference",
        )

        workflow = gr.Radio(
            choices=[
                "Analysis",
                "Recipe",
            ],
            value="Analysis",
            label="⚙️ Workflow",
        )

        output = gr.Textbox(
            label="📄 Result",
            lines=25,
        )

        analyze_button = gr.Button("🚀 Analyze")

        analyze_button.click(
            fn=process_food,
            inputs=[
                image_input,
                diet,
                workflow,
            ],
            outputs=output,
        )

    return app


def main() -> None:
    """
    Application entry point.
    """

    app = build_interface()
    app.launch()


if __name__ == "__main__":
    main()