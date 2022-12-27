<template>
    <div id="new-task-form">
  
      <!-- TODO: Add a submit event handler attribute to handle the form submission -->
      <!-- HINT: Remember to pass in the form data to the method so it can pass it to your API -->
      <!-- HINT: Also, you can add .prevent to the end of the attribute's key to keep the page from reloading -->
      <v-form @submit.prevent="createTask(form)">
  
        <v-container>
          <v-row>
  
            <v-col cols="12" xs="12" sm="6">
  
              <!-- TODO: Bind this input to the Text property value of the form prop -->
              <v-text-field v-model="form.Text" label="Add a task..." prepend-icon="edit" required></v-text-field>
  
            </v-col>
            <v-col cols="12" xs="12" sm="4">
              <v-menu v-model="menu" :close-on-content-click="false" :nudge-right="40" transition="scale-transition" offset-y min-width="290px">
                <template v-slot:activator="{ on }">
  
                  <!-- TODO: Bind this input to the Date property value of the form prop -->
                  <v-text-field v-model="form.Date" label="When should the task be done?" prepend-icon="event" v-on="on"></v-text-field>
  
                </template>
  
                <!-- TODO: Also bind this input to the Date property value of the form prop -->
                <v-date-picker @input="menu = false"></v-date-picker>
  
              </v-menu>
            </v-col>
            <v-col cols="12" xs="4" offset-xs="4" sm="2">
              <v-btn class="mt-3" type="submit" text color="success" block>
                <v-icon left>mdi-plus</v-icon>
                Add Task
              </v-btn>
            </v-col>
          </v-row>
        </v-container>
      </v-form>
    </div>
  </template>
  
  <script>
  import { getCurrentDate } from '@/util'
  export default {
    name: 'NewTaskForm',
    props: {
      // TODO: Figure out any props that you'll need from this component's parent and add it/them here
      form:{
        Text: "",
        Date: getCurrentDate()
      },

      createTask: {
        type: Function
      }

    },
    data: () => ({
      menu: false,
    }),
  }
  </script>
  
  <style scoped>
  form {
    padding: 0 1rem;
  }
  </style>