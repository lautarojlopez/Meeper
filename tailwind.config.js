const colors = require('tailwindcss/colors')

module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    fontFamily:{
      'poppins': ['Poppins', 'sans-serif'],
      'times': ["Times New Roman", 'Times', 'serif'],
      'nunito': "Nunito, sans-serif"
    },
    extend: {
      colors:{
        teal: colors.teal,
        emerald: colors.emerald,
        lime: colors.lime,
        bluegray: colors.blueGray
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
