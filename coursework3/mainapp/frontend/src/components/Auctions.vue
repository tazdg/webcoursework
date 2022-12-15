<template>
    <div class="auctions">
        <br>
        <h2 >Auctions Page</h2>
        <br>
        <p>Here you can see all of the auctions being currently held and bid in those auctions</p>
    </div>

    <div>
      <!-- Search Bar -->
      <h6 class="mt-5">Search</h6>
      <div class="input-group mb-5 justify-content-center">
        <input
          class="bg-light text-dark w-50 rounded border border-info border-3"
          type="text"
          v-model="search"
          placeholder="Search items by title or description..."
        />
      </div>

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

        <tr v-for="item in filteredItems">
          <td>{{item.title}}</td>
          <td>{{item.description}}</td>
          <td><a href="http://localhost:8000{{item.image}}"><img :src="'http://localhost:8000'+item.image" width="140" height="140"/></a></td>
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
            search: ''
        };
    },
    mounted() {
      this.fetch_items()
      console.log(`the component is now mounted.`)
  },

    methods: {
        // async fetch_items() {
        //     //Perform Ajax request to fetch list of items
        //     console.log(`fetching..`)
        //     let response = await fetch("http://localhost:8000/mainapp/api/items/");
        //     let data = await response.json();
        //     this.items = data.items;
        // },

      async fetch_items() {
        //Perform Ajax request to fetch list of items
        console.log(`fetching..`)
        let response = await fetch("http://localhost:8000/mainapp/api/items/",
        {
          credentials: 
          "include",

          mode: 
          "cors",

          referrerPolicy: 
          "no-referrer",
        }

        );
        let data = await response.json();
        this.items = data.items;
      },
    },

    computed: {
      filteredItems(){
        let filteredItems = this.items.filter((item) => {
          return item.title.toLowerCase().includes(this.search.toLowerCase()) + item.description.toLowerCase().includes(this.search.toLowerCase());
        })
        let orderedItems = filteredItems.sort((a,b) => {
          return b.upvoted - a.upvoted;
        })        
        return orderedItems;
      }
    }

}
</script>