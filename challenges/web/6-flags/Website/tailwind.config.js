/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./**/*.{html}",
    "./static/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'my-black': '#18181B',
        'my-gray': '#2F2F36',
        'dark-blue': '#577399',
        'light-blue': '#BDD5EA',
        'my-white': '#F7F7FF',
        'red': '#FE5F55',
        'very-dark-blue': '#495867', 
        'my-red': '#FE5758',
        'my-yellow': '#FFEEAB',
      }
    },
  },
  plugins: [],
}

