import { ArrowRight } from "lucide-react";
import logo from "../../assets/logo.png";

function Navbar() {
  return (
    <header className="sticky top-0 z-50 border-b border-green-100 bg-[#FFFDF7]/90 backdrop-blur-md">
      <div className="mx-auto flex h-24 max-w-7xl items-center justify-between px-8">

        {/* Logo */}
        <div className="flex items-center gap-3 cursor-pointer">

          <img
            src={logo}
            alt="NourishBot Logo"
            className="h-16 w-16 object-contain"
          />

          <h1 className="text-3xl font-bold text-[#1B4332]">
            Nourish<span className="text-green-600">Bot</span>
          </h1>

        </div>

        {/* Navigation */}
        <nav className="hidden lg:flex items-center gap-10 text-lg font-medium text-slate-700">
          <a href="#" className="text-green-600 border-b-2 border-green-600 pb-1">
            Home
          </a>

          <a href="#" className="hover:text-green-600 transition">
            Features
          </a>

          <a href="#" className="hover:text-green-600 transition">
            How It Works
          </a>

          <a href="#" className="hover:text-green-600 transition">
            Recipes
          </a>

          <a href="#" className="hover:text-green-600 transition">
            About
          </a>
        </nav>

        {/* Button */}
        <button className="flex items-center gap-2 rounded-full bg-green-600 px-7 py-3 text-lg font-semibold text-white transition hover:bg-green-700">
          Scan Meal
          <ArrowRight size={20} />
        </button>

      </div>
    </header>
  );
}

export default Navbar;