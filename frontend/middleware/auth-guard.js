import { useUserStore } from '@/stores/user';

export default defineNuxtRouteMiddleware((to, from) => {
    console.log(to)
    const userStore = useUserStore()  
    if ((to.path === '/account/register' || to.path === '/account/login') && userStore.isAuthenticated) {
      return navigateTo('/')
    }
  })
  