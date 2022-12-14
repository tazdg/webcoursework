<template>

<div class="profile">
      <br>
      <h2>Profile Page</h2>
      <br>
  </div>

<div>
<button @click="fetch_Profile">Fetch profile</button>
<div></div> <!--put data here - next thing to sort out-->
</div>
</template>

<script> 
export default{
  data(){
    return{
      profile: [],
    };
  },

  mounted() {
      this.fetch_Profile()
      console.log(`the component is now mounted.`)
  },

  methods:{
      async fetch_Profile(){ // perform an AJAX request to fetch user data 
      let response = await fetch("http://localhost:8000/mainapp/api/profile/")
      let data = await response.json();
      this.profile = data.profile
      console.log("here is your profile")
     }

  } 
}
</script>
