import { useUserStore } from '@/stores/user';

export default defineNuxtRouteMiddleware((to, from) => {
    const userStore = useUserStore()  
    if ((to.path === '/account/register' || to.path === '/account/login') && userStore.isAuthenticated) {
      return navigateTo('/')
    }
  })
  