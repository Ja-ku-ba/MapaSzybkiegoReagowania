import axios from "axios"
import { useUserStore } from '@/stores/user';

export default defineNuxtPlugin((NuxtApp) => {
    const userStore = useUserStore();
    axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'
    if(process.client){
        let token = userStore.authTokens.access
        if(token){
            console.log(token)
            axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        }
    }
    return {
        provide: { 
            axios: axios
        },
    }
})
