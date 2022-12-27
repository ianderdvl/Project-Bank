<template>
    <div class="home">
      <v-card class="mx-auto" max-width="900" v-if="fetched">
        <new-task-form :form="form" :createTask="createTask"/>
        <v-divider></v-divider>
        <v-list subheader two-line flat>
          <v-subheader>
  
            <!-- TODO: use the `user` prop to display the user's username here -->{{user.UserName}}'s Tasks:
  
          </v-subheader>
  
          <!-- TODO: Add your TaskList component -->
          <TaskList :tasks="tasks" :deleteTask="deleteTask" :updateTask="updateTask"></TaskList>
          <!-- Make sure to pass in any necessary props -->
        </v-list>
      </v-card>
    </div>
  </template>
  <script>
  import { getCurrentDate } from '@/util' // No need for formatDate
  import NewTaskForm from '@/components/NewTaskForm.vue'
  import TaskList from '@/components/TaskList.vue'
  // TODO: Import the components you want to use from their files DONE
  export default {
    name: 'Home',
    components: {
      // TODO: Use the Vue Documentation to find out how to use this property DONE

      NewTaskForm,
      TaskList
    },
    props: {

      // TODO: Add the user object as a prop that's passed in from the App.vue component DONE
      user:{

        type: Object, 
        default: {
          type: Object,
          UserName: ""
        }
      }
    },
    data: () => ({ // Populating the data object
      fetched: false,
      tasks: [],
      form: {
        // TODO: Add 2 properties to this form data object to track the Text and the Date
        Text: "",
        Date: getCurrentDate(),
      }
        // HINT: Capitalize the "Text" and "Date" properties to make it easier to pass the data to your API
        // HINT: You can use the `getCurrentDate()` method to get today's date in the proper format for the datepicker
      }),
   
    mounted() {
      // TODO: Call the method that gets the tasks from your API
      this.readTasks()
    },

    methods: { // Defining the actionability of the object

      createTask() {

        // TODO: Use fetch() to send a POST request to your API that includes the data from this.form
        fetch(

         `${process.env.VUE_APP_API_ORIGIN}/api/v1/tasks/`,
        // TODO: Remember to get the updated task list when it's done
        {

            method: `POST`,
            credentials: `include`,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ Text: this.form.Text, Date: this.form.Date})
          }
          ).then(response => {

          if (response.ok) {

            this.readTasks()
          }
        })
        // TODO: Remember to reset the values in this.form to their initial values when it's done
        this.form.Text= ""
        this.form.Date= getCurrentDate()
      },
      readTasks() {

        fetch( // Accesses the tasks endpoint to grab them
          `${process.env.VUE_APP_API_ORIGIN}/api/v1/tasks/`,
          {

            method: `GET`,
            credentials: `include`,
          }
        ).then(response => {

          if (response.ok) {
  
            return response.json()
          }
        })

        .then(response => {

          this.tasks = response;
          console.log(response)
          this.fetched = true;
        })

      },
      updateTask(task) { 

        fetch(
          `${process.env.VUE_APP_API_ORIGIN}/api/v1/tasks/${task._id}`, //  Finds the appropriate task at the tasks enpoint using its id
    
          {

            method: `PUT`,
            credentials: `include`,
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ Done: !task.Done})
  
          }
        ).then(response => {

          if (response.ok) {

            return response.json()
          }
        })
        .then(response => {

        this.readTasks()
        })
      },
      deleteTask(task) {

        fetch(
          `${process.env.VUE_APP_API_ORIGIN}/api/v1/tasks/${task._id}`,
          {

            method: `DELETE`,
            credentials: `include`,
          }
        ).then(response => {

          if (response.ok) {

            this.readTasks()
          }
        })
      }
    }
  }
  </script>

<style scoped>
    .form { 
      /* Necessary? */

        padding: 0 1rem;
    }
</style>