import type { IEvents } from '~/types/event';

export interface IUserEvents {
    username: string,
    email: string,
    date_joined: string,
    events: IEvents;
}
