
<template>
    <div class="new-auction">
        <br>
        <h2>Hold a new Auction</h2>
    </div>

    <div class="border rounded bg-light shadow p-4">
    <form id="logout-form" action="/logout" method="POST" role="form">
      <input type="hidden" name="_token" :value="csrf">
      <input class="form-control m-0.5 center-block" v-model="title" placeholder="Auction Title">
      <br/>
      <input class="form-control m-0.5 center-block" v-model="description" placeholder="Description">

      <!-- Find how to add image -->
      <br/>
      <!-- <input class="form-control m-0.5 center-block" v-on:change="image" type="file" id="img" name="img" accept="image/*"> -->
      <br/>
      <input class="form-control m-0.5 center-block" v-model="starting_price" placeholder="Starting Price">
      <br/>
      <!-- <input class="form-control m-0.5 center-block"  placeholder="Auction Ends"> -->
      <br/>
      <p>Date ends</p>
      <input type="datetime-local" id="birthdaytime" name="birthdaytime" v-model="date_ends">
      <select class="form-control m-0.5 center-block" v-model="available">
        <option value="True">Available</option>
        <option  value="False">Unavailable</option>
      </select>
      
    </form>
  </div>
  
  <button class="bg-success rounded" @click="create_new_item">Create Auction</button>
</template>


<script>
  export default{
    data(){
      return {
        name: "",
        items: [],
        // csrf: document.querySelector('meta[name="csrf-token"]').getAttribute('content')
      }
    },
    
    methods: {
      create_new_item() {
        // const token = localStorage.getItem('token')
        console.log(`Creating new item for auction`)
        fetch("http://localhost:8000/mainapp/api/items/", {

          credentials: 
          "include",

          mode: 
          "cors",

          referrerPolicy: 
          "no-referrer",

          method: "POST",
          
          body: JSON.stringify({
            title: this.title,
            description: this.description,
            // image: this.image,
            starting_price: this.starting_price,
            date_ends: this.date_ends,
            available: this.available,
          })
        });
        
      },
    }
  }

</script>