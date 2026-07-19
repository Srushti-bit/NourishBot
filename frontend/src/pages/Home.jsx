import Navbar from "../components/layout/Navbar";
import Hero from "../components/hero/Hero";
import Features from "../components/sections/Features";

function Home() {
  return (
    <div className="min-h-screen bg-[#F7FCF9]">
      {/* Navigation */}
      <Navbar />

      {/* Hero Section */}
      <Hero />

      {/* Features Section */}
      <Features />
    </div>
  );
}

export default Home;