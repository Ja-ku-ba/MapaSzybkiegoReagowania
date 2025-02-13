import axios from "axios";
import { useUserStore } from "@/stores/user";

export default defineNuxtPlugin((nuxtApp) => {
  // const config = nuxtApp.$config.public;

  const instance = axios.create({
    // baseURL: config.apiUrl
    baseURL: 'http://127.0.0.1:8000/api'
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
