<template>
  
    <header>
      <h1>App.vue</h1>
      <h1>{{app_name}}</h1>
    </header> <!-- The variable app_name is taken from script below -->
    
  <div>

    <!-- <Profile/> -->
  </div>

  <!-- <RouterLink></RouterLink>
  <RouterView></RouterView> -->
  <router-link to="/">Home</router-link>
  <router-link to="/about">About</router-link>
  <router-view></router-view>
</template>


<script>
// import Profile from './components/Profile.vue'
//   export default{

//     components:{
//       Profile,
//     },
//     data(){
//       return{
//         app_name: 'Auction Genie'
//       }
//     },

//     components: { Profile }
//   }
</script>


