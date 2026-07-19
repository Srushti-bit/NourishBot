import { Brain, Salad, UtensilsCrossed } from "lucide-react";

function HeroStats() {
  return (
    <div className="mt-20 grid gap-8 rounded-3xl bg-white p-8 shadow-xl md:grid-cols-3">

      <div className="flex flex-col items-center text-center">
        <div className="mb-4 rounded-2xl bg-green-100 p-4">
          <Brain size={34} className="text-green-600" />
        </div>

        <h3 className="text-xl font-semibold text-slate-800">
          AI Food Recognition
        </h3>

        <p className="mt-2 text-slate-500">
          Detects meals from uploaded food images using computer vision.
        </p>
      </div>

      <div className="flex flex-col items-center text-center">
        <div className="mb-4 rounded-2xl bg-green-100 p-4">
          <Salad size={34} className="text-green-600" />
        </div>

        <h3 className="text-xl font-semibold text-slate-800">
          Nutrition Analysis
        </h3>

        <p className="mt-2 text-slate-500">
          Calculates calories, protein, carbohydrates and fats instantly.
        </p>
      </div>

      <div className="flex flex-col items-center text-center">
        <div className="mb-4 rounded-2xl bg-green-100 p-4">
          <UtensilsCrossed size={34} className="text-green-600" />
        </div>

        <h3 className="text-xl font-semibold text-slate-800">
          Smart Recipe Suggestions
        </h3>

        <p className="mt-2 text-slate-500">
          Generates healthier meal ideas based on detected ingredients and dietary preferences.
        </p>
      </div>

    </div>
  );
}

export default HeroStats;