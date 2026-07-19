import HeroButtons from "./HeroButtons";

function HeroContent() {
  return (
    <div className="max-w-xl">

      <span className="rounded-full bg-green-100 px-4 py-2 text-sm font-semibold text-green-700">
        🥗 AI Nutrition Assistant
      </span>

      <h1 className="mt-8 text-6xl font-extrabold leading-tight text-slate-900">
        Track it.
        <br />
        Trust it.
        <br />
        <span className="text-green-500">
          Transform your habits.
        </span>
      </h1>

      <p className="mt-8 text-lg leading-8 text-slate-500">
        Snap a photo of any meal and get an instant,
        clinical-grade nutrition breakdown with
        personalized recipe suggestions powered by AI.
      </p>

      <HeroButtons />

    </div>
  );
}

export default HeroContent;