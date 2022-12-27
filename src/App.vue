<template>
  <v-app>
    <!-- Link to Material Icons-->
    <link
      href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700|Material+Icons"
      rel="stylesheet"
      type="text/css"
    />
    
    <!-- DONE: Add an AppBar component here -->
    <!-- Make sure to pass in the user object as a prop. -->
    <AppBar :user = "user"></AppBar>

    <v-content>
      <router-view :user="user"></router-view>
    </v-content>

  </v-app>
</template>

<script>
// DONE: Import the app bar component here
// HINT: When writing your import path, you can use the `@` symbol
// to jump straight to the `src` folder instead of trying to figure
// out how to do a relative path. Also, if you're trying to access
// a JavaScript file called `index.js`, you can skip the entire file
// name and just use the containing folder's name; e.g.:
// import thing from '@/util'
// is the same as:
// import thing from '../src/util/index.js'
// Remember, this only works for files called `index.js`. `.vue` files
// must be imported with the entire file name, including the extension.
// e.g.:
// import MyComponent from '@/components/MyComponent.vue'
// You can delete or move these comments if you'd like.
import AppBar from '@/components/AppBar.vue'
export default {
  name: 'App',
  components: {
      // TODO: Use the Vue Documentation to find out how to use this property
      AppBar
  },
  asyncComputed: {
    user: {
      async get() {
        // TODO: Use fetch() to get the user from your API
        // Make sure to include your credentials in the request
        // Also you might want to still return an object identical
        // to the `default` below if the fetch() fails
        const resp = await fetch(`${process.env.VUE_APP_API_ORIGIN}/api/v1/user`, {

          credentials: `include`,
        })
        if(resp.ok) return resp.json();
        else return {UserName: ''}
      },
      default: {
        UserName: ''
      }
    }
  }
}
</script>