import HeroContent from "./HeroContent";
import HeroImage from "./HeroImage";

function Hero() {
  return (
    <section className="min-h-screen overflow-hidden bg-[#F7FCF9]">
      <div className="grid min-h-screen grid-cols-1 lg:grid-cols-2">

        {/* Left Content */}
        <div className="flex items-center px-8 py-20 lg:px-20">
          <HeroContent />
        </div>

        {/* Right Image */}
        <div className="relative flex items-center justify-center">
          <HeroImage />
        </div>

      </div>
    </section>
  );
}

export default Hero;