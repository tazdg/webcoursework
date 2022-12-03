<template>
  <div>
    Welcome to {{app_name}} <!-- The variable app_name is taken from script below -->
    <Profile/>
  </div>
</template>


<script>
import Profile from './components/Profile.vue'
  export default{

    components:{
      Profile,
    },
    data(){
      return{
        app_name: 'Auction Genie'
      }
    },

    components: { Profile }
  }
</script>
