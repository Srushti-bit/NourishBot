import heroImage from "../../assets/illustrations/hero.png";

function HeroImage() {
  return (
    <div className="relative flex justify-center items-center">

      {/* Background Glow */}
      <div className="absolute h-[500px] w-[500px] rounded-full bg-green-200 blur-3xl opacity-40"></div>

      {/* Hero Image */}
      <img
        src={heroImage}
        alt="NourishBot AI Nutrition"
        className="relative z-10 w-full max-w-xl drop-shadow-2xl"
      />

      {/* Floating Card 1 */}
      <div className="absolute top-12 left-0 rounded-3xl bg-white p-5 shadow-xl">
      <p className="text-sm text-gray-500">
🤖 AI Nutrition
      </p>

      <h3 className="text-lg font-bold text-green-600">
Clinical-grade Analysis
      </h3>
      </div>

      {/* Floating Card 2 */}
      <div className="absolute bottom-10 right-0 rounded-3xl bg-white p-5 shadow-xl">
        <p className="text-sm text-gray-500">
         🥗 Personalized
       </p>

        <h3 className="text-lg font-bold text-green-600">
        Recipe Suggestions
        </h3>
      </div>

    </div>
  );
}

export default HeroImage;