<template>
  <div>
    Welcome to {{app_name}} <!-- The variable app_name is taken from script below -->
    
  </div>
</template>


<script>
  export default{
    data(){
      return{
        app_name: 'Auction Genie'
      }
    }
  }
</script>
