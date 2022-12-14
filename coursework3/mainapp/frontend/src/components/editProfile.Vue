<template>
    <div class="edit-Profile">
        <br>
        <h2>Edit Profile</h2>
    </div>

    <div class="border rounded bg-light shadow p-4">
    <div >
      <input class="form-control m-0.5 center-block" v-model="title" placeholder="Edit your profile">
      <br/>
      <input class="form-control m-0.5 center-block" v-model="description" placeholder="Description">

      <!-- Find how to add image to v-model -->
      <br/>
      <input class="form-control m-0.5 center-block" v-on:change="image" type="file" id="img" name="img" accept="image/*">
      <br/>
      <input class="form-control m-0.5 center-block" v-model="starting_price" placeholder="email">
      <br/>
      <!-- <input class="form-control m-0.5 center-block"  placeholder="Auction Ends"> -->
      <br/>
      <p>Date ends</p>
      <input type="datetime-local" id="birthdaytime" name="birthdaytime" v-model="date_ends">
      
    </div>
  </div>
  
  <button class="bg-success rounded" @click="edit_Profile">Save changes</button>
</template>
  
<script>
  export default{
    data(){
      return {
        name: ""
      }
    },
    
    methods: {
      edit_Profile() {
        console.log(`Saving profile changes'${this.title}`)
        fetch("http://localhost:8000/mainapp/api/profile/", {
          method: "POST",
          body: JSON.stringify({
            username: this.username,
            firstname: this.description,
            email: this.email,
            // image: this.image,
          })
        })
      },
    }
  }


</script>