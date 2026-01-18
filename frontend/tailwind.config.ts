import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/**/*.{js,ts,jsx,tsx,mdx}",  // Add this line
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
      },
      animation: {
        'bounce': 'bounce 1s infinite',
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
  // Add safelist via type assertion (valid Tailwind option, not in TS types)
  safelist: ['max-w-2xl', 'max-w-3xl', 'mx-auto'],
} as Config & { safelist?: string[] };

export default config;


