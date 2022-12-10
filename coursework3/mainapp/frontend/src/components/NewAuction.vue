<template>
    <div class="new-auction">
        <br>
        <h2>Hold a new Auction</h2>
    </div>

    <div class="border rounded bg-light shadow p-4">
    <div >
      <input class="form-control m-0.5 center-block" v-model="title" placeholder="Auction Title">
      <br/>
      <input class="form-control m-0.5 center-block" v-model="description" placeholder="Description">

      <!-- Find how to add image to v-model -->
      <br/>
      <input class="form-control m-0.5 center-block" v-on:change="image" type="file" id="img" name="img" accept="image/*">
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
      
    </div>
  </div>
  
  <button class="bg-success rounded" @click="create_new_item">Create Auction</button>
</template>
  
<script>
  export default{
    data(){
      return {
        name: ""
      }
    },
    
    methods: {
      create_new_item() {
        console.log(`Creating new item for auction ${this.title}`)
        fetch("http://localhost:8000/mainapp/api/items/", {
          method: "POST",
          body: JSON.stringify({
            title: this.title,
            description: this.description,
            // image: this.image,
            starting_price: this.starting_price,
            date_ends: this.date_ends,
            available: this.available,
          })
        })
      },
    }
  }

    // $(function () {
    //     // connecting click on profile image with click on upload file button
    //     $('#profile-img').click(function() {
    //         console.log('Uploading image...')
    //         $("#img_file").click()
    //     });

    //     $('#img_file').change(function uploadFile() {
    //         var formdata = new FormData()
    //         var file = document.getElementById('img_file').files[0]
    //         formdata.append('img_file', file)
    //         formdata.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val())
    //         $.ajax({
    //             type : 'POST',
    //             url  : "{% url 'mainapp:uploadimage api' %}",
    //             data : formdata,
    //             success: function(data) {
    //                 $('#profile-img').attr("src",data);
    //             },
    //             processData : false,
    //             contentType : false,
    //         })
    //     })
    // })

</script>