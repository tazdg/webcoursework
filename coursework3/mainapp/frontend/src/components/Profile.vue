<template>

<div class="profile">
      <br>
      <h2>Profile Page</h2>
      <br>
  </div>

<div>
<div><!--put data here - next thing to sort out-->
    <p id="display-username"> </p>

</div>
</div>
</template>


<script>
export default{ 
    data() {
        return {
            profiles:[],
        };
    },
    mounted() {
      this.fetch_profile()
      console.log(`the component is now mounted.`)
  },

    methods: {
        async fetch_profile() {
            //Perform Ajax request to fetch list of items
            console.log(`fetching..`)
            let response = await fetch("http://localhost:8000/mainapp/api/profile/");
            console.log('here')
            let data = await response.json();// data receives javascript object
            this.profiles = data.profiles;
            console.log('here are your profile details')
            console.log(JSON.stringify(data)); //to check contents of JS object 
            const objj = JSON.stringify(data);
           
            const smth = JSON.parse(objj) //returns the type of the 
            console.log(smth)
 
          
        },
    },

}

</script>



