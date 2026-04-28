import type { Config } from "tailwindcss";

const config: Config = {
  darkMode: ["class"],
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        accent: "#FF6600",
        "accent-d": "#CC5200",
        black: "#050505",
        dark: "#0d0d0d",
        dark2: "#141414",
        light: "#F5F0E8",
        border: "#050505",
      },
      fontFamily: {
        sans: ["Montserrat", "sans-serif"],
        mono: ["Montserrat", "sans-serif"],
      },
      boxShadow: {
        cartoon: "0 4px 0 #050505",
        "cartoon-sm": "0 2px 0 #050505",
        "cartoon-lg": "0 6px 0 #050505",
      },
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
    },
  },
  plugins: [],
};

export default config;
