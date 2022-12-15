<template>

  <!-- Navbar template based on https://getbootstrap.com/docs/4.0/components/navbar/-->
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">  
</head>

<div>
<nav class="navbar navbar-expand-sm navbar-light bg-light fixed-top">
  <a class="navbar-brand text-light" href="#">__</a>
  <a class="navbar-brand text-info" href="#">Auction Genie</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active"><router-link to="/about" class="nav-link">About</router-link></li>
      <li class="nav-item active"><router-link to="/" class="nav-link">Auctions</router-link></li>
      <li class="nav-item active"><router-link to="/new-auction" class="nav-link">New Auction</router-link></li>
      <li class="nav-item active"><router-link to="/messages" class="nav-link">Messages</router-link></li>
      <li class="nav-item active"><router-link to="/profile" class="nav-link">Profile</router-link></li>
      <li class="nav-item active"><router-link to="/test" class="nav-link">Test</router-link></li>
      <li class="text-light">____</li>
      <li class="nav-item activ border border-info border-3 rounded"><a class="btn" @click="logout()">Log Out</a></li>
    </ul>


    <!-- Search Function -->
<!-- 
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
    </form> -->
  </div>
</nav>


    <header>
      <br>
      <br>
      <h5>Welcome to</h5>
      <h1 class="text-info">{{app_name}}</h1>
    </header> <!-- The variable app_name is taken from script below -->
    

    
  <div>

    <!-- <Profile/> -->
  </div>

  <!-- <router-link to="/">Home</router-link>
  <router-link to="/about">About</router-link> -->

  <!-- Displays the components -->
  <router-view></router-view> 
</div>
</template>


<script>
// import Profile from './components/Profile.vue'
  export default{

    components:{
      // Profile,
    },
    data(){
      return{
        app_name: 'Auction Genie'
      }
    },
    methods:{
      async logout(){
        console.log(`fetching..`)
        let response = await fetch("http://localhost:8000/mainapp/logout",
        {
          credentials: 
          "include",

          mode: 
          "cors",

          referrerPolicy: 
          "no-referrer",
        }
        );

        if (response.ok){
          window.location.replace('http://localhost:8000/mainapp/login')
        }
      }

    }
    // components: { Profile }
  }


</script>


