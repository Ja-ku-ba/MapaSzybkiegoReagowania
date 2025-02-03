<template>
    <q-dialog v-model="showAddPointDialog">
      <q-stepper
        v-model="step"
        ref="stepper"
        animated
        class="full-width"
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
            <q-btn v-if="step > 0 && step < 2" @click="processEvent()" color="primary" :label="step === 2 ? 'Zakończ' : 'Dalej'" class="q-ml-auto" />
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
import { useEventStore } from '~/stores/event';
import FirstStep from './AddPoint/FirstStep.vue'
import SecondStep from './AddPoint/SecondStep.vue'
import ThirdStep from './AddPoint/ThirdStep.vue'

const stepper = useState<any>(() => null);
const eventStore = useEventStore();
const showAddPointDialog = useState<boolean>('showAddPointDialog', () => false)
const step = useState<number>('addPointStep', () => 0)

const doAssigments = (n: number) => {
  step.value=n
  eventStore.type = n
}

const processEvent = async () => {
  if (step.value < 2) {
    stepper.value?.next()
  } else {
    const resp = await eventStore.sendEvent()
    if (resp) {
      step.value = 9
    }
  }
}
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