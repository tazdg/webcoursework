<template>
  
    <header>
      <h1>{{app_name}}</h1>
    </header> <!-- The variable app_name is taken from script below -->
    
  <div>

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
