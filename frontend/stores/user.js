import { defineStore } from "pinia";
import { jwtDecode } from 'jwt-decode';

export const useUserStore = defineStore('user', {
    state: () => ({
        user: null,
        isAuthenticated: false,
        authTokens: null,
        refreshTimeout: null,
    }),
    actions: {
        async login(email, password) {
            const BASE_URL = useRuntimeConfig().public.baseUrl;
            try {
                const response = await $fetch(`${BASE_URL}/account/api/token/`, {
                    method: 'POST',
                    body: JSON.stringify({ email, password }),
                });
                const authTokens = response;
                const user = jwtDecode(authTokens.access);
                this.user = user;
                this.authTokens = authTokens;
                this.isAuthenticated = true;

                this.startTokenRefresh();
                navigateTo('/', {external: true})
                return true
            } catch (error) {
                console.error("Login error:", error);
                return false
            }
        },

        startTokenRefresh() {
            if (this.refreshTimeout) clearTimeout(this.refreshTimeout);

            const user = this.user;
            if (!user) return;

            const currentTime = Math.floor(Date.now() / 1000);
            const timeToExpire = user.exp - currentTime;

            const refreshTime = timeToExpire - 30 > 0 ? timeToExpire - 10 : 1;

            this.refreshTimeout = setTimeout(() => {
                this.refreshToken();
            }, refreshTime * 1000);
        },

        stopTokenRefresh() {
            if (this.refreshTimeout) {
                clearTimeout(this.refreshTimeout);
                this.refreshTimeout = null;
            }
        },

        async refreshToken() {
            try {
                const BASE_URL = useRuntimeConfig().public.baseUrl;
                if (!this.authTokens?.refresh) {
                    this.logout();
                    return;
                }

                const refreshToken = this.authTokens.refresh;
                const response = await $fetch(`${BASE_URL}/account/api/token/refresh/`, {
                    method: "POST",
                    body: { refresh: refreshToken },
                });

                this.authTokens.access = response.access;
                this.user = jwtDecode(response.access);

                this.startTokenRefresh();
            } catch (error) {
                this.logout();
            }
        },

        logout() {
            this.user = null;
            this.authTokens = null;
            this.isAuthenticated = false;
            this.stopTokenRefresh();
        
            // navigateTo('/')
            // window.location.reload()
        }
    },
    persist: true,
});