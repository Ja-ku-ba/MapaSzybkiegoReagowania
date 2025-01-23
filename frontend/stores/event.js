import { defineStore } from "pinia";

export const useEventStore = defineStore('event', {
    state: () => ({
        userToken: null,
        latitiude: null,
        longnitiude: null,
        description: null,
        showDescription: false,
        type: null,
    }),
    actions: {
        validateEvent() {
            let messages = []
            if (this.latitiude === null || this.longnitiude === null) { 
                messages.push('Niestety nie wiemy w jakim miejscu chcesz dodać zgłoszenie')
            } 
            if (description === null || description.length < 5) {
                messages.push('Niestety nie wiemy co chcesz nam powiedzieć o zdarzenieu')
            }

            // do sprawdzenia czy array sie zeruje po odswiezeniu
            if (messages === []) {
                sendEvent()
            }
            return messages
        },
        sendEvent() {
            console.log("Wysyłanie wventu")
        }
    },
    persist: true,
});
