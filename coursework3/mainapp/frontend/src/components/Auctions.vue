<template>
    <div class="auctions">
        <br>
        <h2 >Auctions Page</h2>
        <br>
        <p>Here you can see all of the auctions being currently held and bid in those auctions</p>
    </div>

    <div>
        <button class="rounded" @click="fetch_items">Fetch items (remove button later)</button>
        <table class="table table-bordered">
        <tr>
          <th>Title</th>
          <th>Description</th>
          <th>Picture</th>
          <th>Price</th>
          <th>Auction Ends</th>
          <th></th>
          <th></th>
          <th></th>
        </tr>

        <tr v-for="item in items">
          <td>{{item.title}}</td>

          <td>{{item.description}}</td>
          <td><a href="http://localhost:8000'{{item.image}}"><img src="http://localhost:8000{{item.image}}" width="140" height="140"/></a></td>

          <td>£{{item.starting_price}}</td>
          <td>Auction Ends: {{item.date_ends}}</td>
          <td v-if="item.available">(Available)</td>
          <td v-if="!item.available">(Unavailable)</td>
          <td><button class="bg-primary rounded">Message Seller</button></td>
          <td><button class="bg-success rounded" @click="delete_scan(scan)">Bid</button></td>
        </tr>
      </table>
    </div>

</template>
  
<script>
export default{ 
    data() {
        return {
            items: [],
        };
    },
    mounted() {
      this.fetch_items()
      console.log(`the component is now mounted.`)
  },

    methods: {
        async fetch_items() {
            //Perform Ajax request to fetch list of items
            console.log(`fetching..`)
            let response = await fetch("http://localhost:8000/mainapp/api/items/");
            let data = await response.json();
            this.items = data.items;
        },
    },

}
</script>