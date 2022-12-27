<template>
    <div id='app-bar'>
      <v-app-bar app color="primary" dark>
  
        <v-toolbar-title>Todo App</v-toolbar-title>
  
        <v-spacer></v-spacer>
  
        <!-- TODO: Use a v-if to only show this button when the user is logged in -->
        <v-btn v-if="loggedIn" icon v-on:click.stop="drawer = !drawer">
          <v-icon>mdi-menu</v-icon>
        </v-btn>
      </v-app-bar>
  
      <v-navigation-drawer v-model="drawer" absolute temporary right>
        <v-list-item>
  
          <!-- TODO (extra-credit): If you choose to do the extra credit, comment out the following line -->
          <v-list-item-title>{{user.UserName}}</v-list-item-title>
            
          <!-- TODO (extra-credit): This is where you would put the image you get from Google's OAuth 2 scope -->
          <!-- If the image's URL is a string on the user object, pass it into the :src attribute -->
          <!-- <v-list-item-avatar> -->
          <!-- <v-img :src=""></v-img> -->
          <!-- </v-list-item-avatar> -->
  
          <!-- TODO (extra-credit): This is where you would put the user's email from Google -->
          <!-- Remember, use mustache syntax {{}} to pass the value of a variable into this HTML -->
          <!-- <v-list-item-content> -->
          <!-- <v-list-item-title></v-list-item-title> -->
          <!-- </v-list-item-content> -->
  
        </v-list-item>
  
        <v-divider></v-divider>
  
        <v-list dense>
  
          <!-- TODO: Add an :href attribute to this tag so that clicking this link will log a user out -->
          <v-list-item :href="`${apiOrigin}/api/v1/auth/logout`" link>
  
            <!-- HINT: When there's a colon before an attribute, that's a short-hand for v-bind: which means -->
            <!-- that in the quotation marks of that attribute, you can put JavaScript! That means you can -->
            <!-- use a backtick string to concatenate the API origin env variable to the logout path! -->
  
            <v-list-item-icon>
              <v-icon>mdi-logout-variant</v-icon>
            </v-list-item-icon>
  
            <v-list-item-content>
              <v-list-item-title>Log Out</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </div>
  </template>
  
  <script>
  import { authenticated } from '@/util'
  export default {
    name: 'AppBar',
    props: {
      // TODO: Pass in the user object to this component as a prop
      // Make sure to give it a default value that has the UserName defined as an empty string
        user: {
            Type: Object,
            Default: {
                Type: Object,
                UserName: ""
            }
        }
    },
    data: () => ({
      drawer: false,
      // TODO: Get the api's url origin from process.env and set it to a variable here
        apiOrigin: process.env.VUE_APP_API_ORIGIN
    }),
    asyncComputed: {
      loggedIn: {
        get: async () => await authenticated(),
        default: false
      },
    }
  }
  </script>