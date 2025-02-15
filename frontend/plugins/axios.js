import axios from "axios";
import { useUserStore } from "@/stores/user";

export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig();

  const instance = axios.create({
    baseURL: config.public.baseUrl
  });

  if (import.meta.client) {
    const userStore = useUserStore();
    const token = userStore.authTokens?.access;
    if (token) {
      instance.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    }
  }

  return {
    provide: {
      axios: instance,
    },
  };
});
