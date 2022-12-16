<template>
    <div class="bid">
        <br>
        <h2>Bid Page</h2>
        <br>
        <p> Here you can place a bid on the auction item you clicked in the auctions page </p>

        <!-- print item's details -->
        <div v-for="(item, id) in fetch_item_details">
            <a href="http://localhost:8000'{{item.image}}"><img src="http://localhost:8000{{item.image}}" width="200" height="200"/></a>
            <h2>{{ item.title }}</h2>
            <h3>{{ item.description }}</h3>
            <p>Price: {{ item.starting_price }}</p>
            <br>
            <p>This auction will close at {{ item.date_ends }}</p>
            <br>
            <p>There are currently {{ item.number_of_bids }} bid(s) on this item.</p>
        </div>
        
        <!-- bid form so user can put in their bids for the item -->
        <form id="bid_form" method="POST" action="#">
            <label for="currency-field" class="mt-5">Enter Your Bid Amount:</label>
            <br>
            <input id="bid_price" type="text" name="currency-field" class="mt-3" placeholder="..." pattern="^\\$?(([1-9](\\d*|\\d{0,2}(,\\d{3})*))|0)(\\.\\d{1,2})?$" data-type="currency" autocomplete="off" required v-model="bid_amount">
            <br>
            <label>Bid Amount: £{{ bid_price }}</label>
            <br>
            <button type="submit" class="bg-primary rounded mt-3" @click="place_bid(bid)">Place Bid</button>
        </form>           
    </div>
</template>


<script>
export default { 
    data() {
        return {
            items: [],
            bids: [],
            bid_price: '',
        };
    },
    methods: {
        async fetch_item_details(item) {
            // fetch specific item object's details based on their id
            console.log(`fetching.. ${item.id}`)
            let response = await fetch(`http://localhost:8000/api/item/${item.id}/`);
            let data = await response.json();
            this.items = data.items;
        },

        check_bid_currency() {
            // formats bid_amount to GBP currency format
            let form = document.querySelector('#bid_form');
            let inputField = document.querySelector('bid_price');
            
            form.addEventListener('submit', (e) => {
                e.preventDefault();
            
                let amount = inputField.value;
                let formatted = new Intl.NumberFormat("en-GB", {
                    style: 'currency',
                    currency: 'GBP'
                }).format(amount);

                inputField.value = formatted;
            })
        },

        validate_bid() {
            // ensures bid_amount is larger than starting_price
            let bid_price = this.bid_price;
            let starting_bid = items.starting_bid;

            if (Number(bid_price) < starting_bid) {
                alert("Your bid amount needs to be more than the item's starting bid");
                return false;
            }
        },

        place_bid() {
            // saves user input into the database (Bid model)
            bid = Bid.objects.get(id = bid.id)
            body = json.loads(request.body)

            bid.user_id = this.bids.filter(bid => bid.user_id)
            bid.item_id = this.bids.filter(bid => bid.item_id)
            bid.bid_price = body['bid_price']
            bid.save()

            return JsonResponse(bid.to_dict())
        }
    }
}
</script>