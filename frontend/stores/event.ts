import { defineStore } from "pinia";

interface EventState {
  latitiude: string;
  longitude: string;
  description: string;
  showDescription: boolean;
  type: number | null;
}

export const useEventStore = defineStore('event', {
  state: (): EventState => ({
    latitiude: '',
    longitude: '',
    description: '',
    showDescription: false,
    type: null,
  }),
  actions: {
    validateEvent(): string[] {
      const messages: string[] = [];

      if (!this.latitiude || !this.longitude) {
        messages.push('Niestety nie wiemy w jakim miejscu chcesz dodać zgłoszenie');
      }
      if (!this.description || this.description.length < 5) {
        messages.push('Niestety nie wiemy co chcesz nam powiedzieć o zdarzeniu');
      }

      if (messages.length === 0) {
        this.sendEvent();
      }

      return messages;
    },
    async sendEvent(): Promise<boolean> {
      const { $axios, $q } = useNuxtApp();

      try {
        await $axios.post('event/create/', {
          latitiude: this.latitiude,
          longitude: this.longitude,
          description: this.description,
          type: this.type,
        })

        $q.notify({
          color: 'warning',
          textColor: 'white',
          icon: 'cloud_done',
          position: 'top',
          message: 'Zdarzenie dodane pomyślnie, zobaczysz je na mapie w ciągu 5 minut'
        });

        return true
      } catch (error) {
        $q.notify({
          color: 'warning',
          textColor: 'white',
          icon: 'error',
          position: 'top',
          message: 'Coś poszło nie tak'
        });
      }
      return false
    },
    resetState(): void {
      this.latitiude = '';
      this.longitude = '';
      this.description = '';
      this.showDescription = false;
      this.type = null;
    },
    validState(): boolean {
      return (
        this.latitiude !== '' &&
        this.longitude !== '' &&
        this.description !== '' &&
        this.type !== null
      );
    }
  },
  persist: true
});
