import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  // Override via SITE_URL env var at build time (see .env.example).
  site: process.env.SITE_URL || 'http://localhost:4321',
  output: 'static',
});
