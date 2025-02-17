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
          <FirstStep @nextStep="step=1"/>
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
            <q-btn v-if="stepperShow()" @click="processEvent()" color="primary" 
              :label="finishFinalStep() ? `Zakończ` : `Dalej`" class="q-ml-auto" />
          </q-stepper-navigation>
        </template>
      </q-stepper>
    </q-dialog>
    <div v-if="!showAddPointDialog" class="q-pa-md q-gutter-lg add-point-container show-above-map">
        <q-btn size="24px" round color="primary" icon="add" @click="showAddPointDialog=true">
            <q-tooltip>Dodaj nowe zdarzenie</q-tooltip>
        </q-btn>
    </div> 
</template>

<script setup lang="ts">
import FirstStep from './AddPoint/FirstStep.vue'
import SecondStep from './AddPoint/SecondStep.vue'
import ThirdStep from './AddPoint/ThirdStep.vue'

const stepper = useState<any>(() => null);
const eventStore = useEventStore();
const showAddPointDialog = useState<boolean>('showAddPointDialog', () => false)
const step = useState<number>('addPointStep', () => 0)

const stepperShow = ():boolean => {
  if (step.value !== 2) {
    return step.value > 0
  } else {
    return eventStore.validState()
  }
}

const finishFinalStep = ():boolean => {
  return step.value === 2 && eventStore.validState()
}

const processEvent = async () => {
  if (step.value < 2) {
    stepper.value?.next()
  } else {
    const resp = await eventStore.sendEvent();

    if (resp) {
      showAddPointDialog.value = false;
      eventStore.resetState()
      step.value = 0
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
    bottom: 25px;
    right: 15px;
}

.select-event-icon {
    border: 1px solid grey;
    padding: 10px;
    border-radius: 50px;
    color: grey;
}


.show-above-map {
  z-index: 1100;
}
</style>