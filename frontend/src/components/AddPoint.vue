<template>
    <q-dialog v-model="showAddPointDialog">
      <q-stepper
        v-model="step"
        ref="stepper"
        animated
      >
        <q-step
          :name="0"
          title=""
        >
          <FirstStep @setStep="(n:number) => doAssigments(n)"/>
        </q-step>

        <q-step
          :name="1"
          title=""
        >
          <SecondStep />
        </q-step>

        <q-step
          :name="2"
          title=""
        >
          <ThirdStep />
        </q-step>

        <template v-slot:navigation>
          <q-stepper-navigation class="full-width flex justify-between">
            <q-btn v-if="step > 0" flat color="primary" @click="$refs.stepper?.previous()" label="Cofnij" />
            <q-btn @click="$refs.stepper?.next()" color="primary" :label="step === 4 ? 'Zakończ' : 'Dalej'" class="q-ml-auto" />
          </q-stepper-navigation>
        </template>
      </q-stepper>
    </q-dialog>

    <div v-if="!showAddPointDialog" class="q-pa-md q-gutter-lg add-point-container">
        <q-btn size="24px" round color="primary" icon="add" @click="showAddPointDialog=true">
            <q-tooltip>Dodaj nowe zdarzenie</q-tooltip>
        </q-btn>
    </div> 
</template>

<script setup lang="ts">
import FirstStep from './AddPoint/FirstStep.vue'
import SecondStep from './AddPoint/SecondStep.vue'
import ThirdStep from './AddPoint/ThirdStep.vue'

const showAddPointDialog = useState<boolean>('showAddPointDialog', () => false)
const step = useState<number>('addPointStep', () => 0)

const doAssigments = (n: number) => {
  step.value=n
  eventStore.type = n
}


import { useEventStore } from '~~/stores/event';

const eventStore = useEventStore();
</script>

<style lang="scss" scoped>
.q-btn ::deep(.q-btn_content) {
  justify-content: start;
}

.add-point-container {
    position: fixed;
    bottom: 15px;
    right: 15px;
}

.select-event-icon {
    border: 1px solid grey;
    padding: 10px;
    border-radius: 50px;
    color: grey;
}
</style>