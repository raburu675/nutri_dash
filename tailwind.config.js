// tailwind.config.js
module.exports = {
  content: [
    "./myapp/templates/**/*.html", // <--- THIS IS CRUCIAL
    // If you have project-level templates, add:
    // "./templates/**/*.html",
    // Add any other file types that might contain Tailwind classes (e.g., if you add JS later)
    // "./**/*.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}