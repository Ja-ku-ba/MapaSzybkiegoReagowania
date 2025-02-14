export default defineNuxtPlugin((nuxtApp) => {
    const progress = ref<number>(0)
    const isLoading = ref(false)

    const start = () => {
      progress.value = 10
      isLoading.value = true
      incrementProgress()
    }
  
    const incrementProgress = () => {
      if (progress.value < 90) {
        setTimeout(() => {
          progress.value += Math.random() * 10
          incrementProgress()
        }, 200)
      }
    }
  
    const stop = () => {
      progress.value = 100
      setTimeout(() => {
        isLoading.value = false
        progress.value = 0
      }, 1500)
    }
  
    nuxtApp.provide("loading", { start, stop, isLoading, progress })
  
    nuxtApp.hook("app:created", () => {
      const router = useRouter()
      router.beforeEach((to, from, next) => {
        start()
        next()
      })
      router.afterEach(() => {
        stop()
      })
    })
  })
  