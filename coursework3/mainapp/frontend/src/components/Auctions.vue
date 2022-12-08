<template>
    <div class="auctions">
        <br>
        <h2 >Auctions Page</h2>
        <br>
        <p>Here you can see all of the auctions being currently held and bid in those auctions</p>
    </div>

    <div>
        <button class="rounded" @click="fetch_items">Fetch items</button>
        <table class="table table-bordered">
        <tr>
          <th>Title</th>
          <th>Description</th>
          <th>Picture</th>
          <th>Price</th>
          <th>Auction Ends</th>
          <th></th>
          <th></th>
        </tr>

        <tr v-for="item in items">
          <td>{{item.title}}</td>
          <td>{{item.description}}</td>
          <td v-if="scan.available">(Available)</td>
          <td v-if="!scan.available">(Unavailable)</td>
          <td>£{{scan.price}}</td>
          <td>Approx appointment time: {{scan.appointment_time}}</td>
          <td><button class="bg-warning rounded">Edit</button></td>
          <td><button class="bg-danger rounded" @click="delete_scan(scan)">Delete</button></td>
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
            //Perform Ajax request to fetch list of scans
            console.log(`fetching..`)
            let response = await fetch("http://localhost:8000/api/items/");
            let data = await response.json();
            this.scans = data.scans;
        },

        
        async delete_scan(scan){
          console.log(`Deleting scan, ${scan.id}`)
          let response = await fetch(`http://localhost:8000/api/scan/${scan.id}/`, {
            method: 'DELETE',
            // body: JSON.stringify({
            //   scan_id: this.scan_id
            // })
          })
          if (response.ok){this.scans = this.scans.filter(s => s.id != scan.id);}
          else{alert('Deleting scan failed');}
      }
    },

}
</script>