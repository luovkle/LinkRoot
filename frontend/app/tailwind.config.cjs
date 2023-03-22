/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      screens: {
        'sm': '360px'
      },
      fontFamily: {
        'logo': ['Lobster', 'sans']
      },
      flex: {
        '2': '2 2 0%',
        '4': '4 4 0%',
      }
    },
  },
  plugins: [],
};
