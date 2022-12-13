<template>
  <div class="auctions">
    <br>
    <h2>Auctions Page</h2>
    <br>
    <p>Here you can see all of the auctions being currently held and bid in those auctions</p>
    
    <div>
      <!-- Search Bar -->
      <div class="input-group mt-5 mb-5 p-3 bg-info justify-content-center">
        <input
          class="bg-warning text-dark"
          type="text"
          v-model="search"
          placeholder="Search items by title.."
        />
      </div>

      <!-- Table containing all auction items --> 
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

        <tr v-for="item in filteredItems">
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
  </div>
</template>
  

<script>
export default{ 
  data() {
    return {
      items: [],
      search: ''
    };
  },
  mounted() {
    this.fetch_items()
    console.log(`the component is now mounted.`)
  },
  methods: {
    async fetch_items() {
      // Perform Ajax request to fetch list of items
      console.log(`fetching..`)
      let response = await fetch("http://localhost:8000/mainapp/api/items/");
      let data = await response.json();
      this.items = data.items;
    },
  },
  computed: {
    filteredItems() {
      // List items based on title & description - includes lower cased ver.
      return this.items.filter(item => item.title.toLowerCase().includes(this.search.toLowerCase()) + item.description.toLowerCase().includes(this.search.toLowerCase())
      );
    }
  }
}
</script>