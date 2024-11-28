// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  modules: ['nuxt-quasar-ui', '@nuxtjs/leaflet'],

  // srcDir: 'src/',
  dir: {
    pages: 'src/pages',
  },
  components: [
    // {
      // path: 'src/components/global', // Katalog dla globalnych komponentów
      // global: true // Komponenty w tym katalogu będą globalnie dostępne
    // },
    'src/components' // Katalog dla komponentów, które będą dostępne lokalnie
  ],
})