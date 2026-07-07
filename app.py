import gradio as gr

from agents.vision_agent import detect_food
from agents.analysis_agent import analyze_meal
from agents.recipe_agent import generate_recipe


def process_food(image, diet, workflow):

    if image is None:
        return "Please upload a food image."

    # Get vision results
    vision_result = detect_food(image)

    detected_foods = vision_result["foods"]
    caption = vision_result["caption"]

    # If no foods were detected
    if not detected_foods:
        return f"""
AI Caption:
{caption}

❌ No known food items were detected.

Try uploading:
• A clearer image
• A closer view of the meal
• Better lighting
"""

    if workflow == "Analysis":

        report = analyze_meal(detected_foods)

        return f"""
=============================
🤖 AI CAPTION
=============================

{caption}

=============================
🍽️ DETECTED FOODS
=============================

{", ".join(detected_foods)}

{report}
"""

    elif workflow == "Recipe":

        recipe = generate_recipe(
            detected_foods,
            diet
        )

        return f"""
=============================
🤖 AI CAPTION
=============================

{caption}

=============================
🍽️ DETECTED FOODS
=============================

{", ".join(detected_foods)}

{recipe}
"""

    return "Invalid workflow selected."


with gr.Blocks(title="🥗 NourishBot") as app:

    gr.Markdown("# 🥗 NourishBot")
    gr.Markdown(
        "Upload a food image to receive AI-powered nutrition analysis or healthy recipe suggestions."
    )

    image_input = gr.Image(
        type="pil",
        label="📷 Upload Food Image"
    )

    diet = gr.Dropdown(
        choices=[
            "None",
            "Vegan",
            "Vegetarian",
            "Gluten-Free",
            "Keto"
        ],
        value="None",
        label="🥦 Diet Preference"
    )

    workflow = gr.Radio(
        choices=[
            "Analysis",
            "Recipe"
        ],
        value="Analysis",
        label="⚙️ Workflow"
    )

    output = gr.Textbox(
        label="📄 Result",
        lines=25
    )

    analyze_button = gr.Button("🚀 Analyze")

    analyze_button.click(
        fn=process_food,
        inputs=[
            image_input,
            diet,
            workflow
        ],
        outputs=output
    )

app.launch()