// nuxt.config.ts
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  runtimeConfig: {
    public: {
      baseUrl: process.env.API_URL,
    }
  },
  app: {
    head: {
      title: 'Mapa szybkiego reagowania',
      meta: [
        { name: 'description', content: 'Projekt na zaliczenie przedmiotu pehape' }
      ],
    },
  },
  devtools: { enabled: true },
  modules: [
    'nuxt-quasar-ui',
    '@nuxtjs/leaflet',
    '@pinia/nuxt',
    'pinia-plugin-persistedstate/nuxt',
  ],
  plugins: [
    '~/plugins/axios.js',
    '~/plugins/loading.ts',
  ],

  quasar: {
    extras: {
      fontIcons: ['material-icons']
    },
    plugins: ['Notify'],
  },

  runtimeConfig: {
    public: {
      apiUrl: process.env.API_URL,
    },
  },
  
  dir: {
    pages: 'src/pages',
  },

  imports: {
    dirs: [
      'types',
    ],
  },

  components: [
    'src/components',
  ],
  
  css: [
    "leaflet/dist/leaflet.css",
    "leaflet.markercluster/dist/MarkerCluster.css",
    "leaflet.markercluster/dist/MarkerCluster.Default.css"
  ],

  leaflet: {
    markerCluster: true
  }
});
