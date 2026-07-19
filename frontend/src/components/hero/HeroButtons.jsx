import { ArrowRight, Camera } from "lucide-react";

function HeroButtons() {
  return (
    <div className="mt-10 flex flex-wrap gap-5">
      <button className="flex items-center gap-3 rounded-2xl bg-green-500 px-8 py-4 text-white font-semibold shadow-lg transition-all duration-300 hover:scale-105 hover:bg-green-600">
        <Camera size={20} />
        Scan my meal
      </button>

      <button className="flex items-center gap-3 rounded-2xl border border-gray-300 bg-white px-8 py-4 font-semibold text-slate-700 shadow-md transition-all duration-300 hover:scale-105">
        View recipes
        <ArrowRight size={18} />
      </button>
    </div>
  );
}

export default HeroButtons;