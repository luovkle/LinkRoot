/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      screens: {
        'sm': '360px'
      },
      fontFamily: {
        'Lobster': ['Lobster', 'cursive']
      },
      flex: {
        '2': '2 2 0%',
        '4': '4 4 0%',
      }
    },
  },
};
