/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      container:"3rem",
      colors: {
        primary: {
          100: '#cb8161',
          // 200: '#f3f4f6',
    },
  },
  },
},
  plugins: [],
}

