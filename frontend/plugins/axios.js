import axios from "axios"

export default defineNuxtPlugin((NuxtApp) => {
    axios.defaults.baseURL = 'http://127.0.0.1:8000/api/'
    // axios.defaults.withCredentials = false;
        // axios.defaults.proxyHeaders = false;
    if(process.client){
        let token = window.localStorage.getItem('authTokens');
        if(token){
            token = JSON.parse(token)
            axios.defaults.headers.common['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM4OTQ0Njk1LCJpYXQiOjE3MzgwODA2OTUsImp0aSI6IjlmNGZkNGRkZWI1NTRjODA5YTFlMmMwYjA2OTE1ZWViIiwidXNlcl9pZCI6MiwidXNlcm5hbWUiOiJzdXBlcnVzZXIifQ.QrLt8KZ4YAgCYntmYl1fzGOQbfpT7KjxTN2XHuQiI_w';
        }
    }
    return {
        provide: { 
            axios: axios
        },
    }
})
