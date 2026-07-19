import {
  Camera,
  Salad,
  UtensilsCrossed,
  HeartPulse,
  Brain,
  Sparkles,
} from "lucide-react";

const features = [
  {
    icon: Camera,
    title: "Scan Your Meal",
    description:
      "Upload a photo of your meal and let NourishBot identify the food.",
  },
  {
    icon: Salad,
    title: "Nutrition Facts",
    description:
      "View calories, protein, carbohydrates, and fats in an easy-to-read format.",
  },
  {
    icon: UtensilsCrossed,
    title: "Healthy Recipes",
    description:
      "Get healthy recipe ideas based on the food you have uploaded.",
  },
  {
    icon: HeartPulse,
    title: "Diet Preferences",
    description:
      "Choose from Vegan, Vegetarian, Keto, or Gluten-Free meal options.",
  },
  {
    icon: Brain,
    title: "Smart AI Analysis",
    description:
      "Receive quick nutrition insights to help you make healthier food choices.",
  },
  {
    icon: Sparkles,
    title: "Simple & Easy",
    description:
      "A clean and easy-to-use experience for tracking your meals every day.",
  },
];

function Features() {
  return (
    <section className="bg-[#F7FCF9] py-24">
      <div className="mx-auto max-w-7xl px-6">

        {/* Heading */}
        <div className="text-center">
          <h2 className="text-5xl font-bold text-slate-900">
            Why Choose{" "}
            <span className="text-green-500">NourishBot?</span>
          </h2>

          <p className="mx-auto mt-6 max-w-3xl text-lg leading-8 text-slate-500">
            NourishBot helps you understand your meals, discover healthier
            recipes, and make better food choices with the power of AI.
          </p>
        </div>

        {/* Feature Cards */}
        <div className="mt-16 grid gap-8 md:grid-cols-2 lg:grid-cols-3">
          {features.map((feature) => {
            const Icon = feature.icon;

            return (
              <div
                key={feature.title}
                className="rounded-3xl bg-white p-8 shadow-lg transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl"
              >
                <div className="mb-6 inline-flex rounded-2xl bg-green-100 p-4">
                  <Icon size={32} className="text-green-600" />
                </div>

                <h3 className="text-2xl font-semibold text-slate-900">
                  {feature.title}
                </h3>

                <p className="mt-4 text-slate-500 leading-7">
                  {feature.description}
                </p>
              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
}

export default Features;