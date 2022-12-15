
<template>
    <br>
    <h2>Messages</h2>
    <p>Display messages sent and recieved here</p>
  

    <div>
      <table class="table table-bordered">
        <tr>
          <th>Sender</th>
          <th>Question</th>
          <th></th>
          <th></th>
          <th></th>
        </tr>

        <tr v-for="questionanswer in questionanswers">
          <td>{{questionanswer.sender}}</td>
          <td>{{questionanswer.recip}}</td>
          <td>____________</td>
          <td>{{questionanswer.text}}</td>
          <td><button class="bg-danger rounded" @click="delete_questionanswer(questionanswer)">Delete</button></td>
        </tr>
      </table>
    </div>
  </template>
  
  <script>
  export default{ 
    data() {
        return {
          questionanswers: [],
        };
    },
    mounted() {
      this.fetch_questionanswers()
      console.log(`the component is now mounted.`)
  },

    methods: {
      async fetch_questionanswers() {
        //Perform Ajax request to fetch list of items
        console.log(`fetching..`)
        let response = await fetch("http://localhost:8000/mainapp/api/questionanswers/",
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
        this.questionanswers = data.questionanswers;
      },
      async delete_questionanswer(questionanswer){
          console.log(`Deleting message, ${questionanswer.id}`)
          let response = await fetch(`http://localhost:8000/api/questionanswer/${questionanswer.id}/`, {
            method: 'DELETE',
          })
          if (response.ok){this.questionanswers = this.questionanswers.filter(s => s.id != questionanswer.id);}
          else{alert('Deleting message failed');}
      }
    },
}

  </script>
  