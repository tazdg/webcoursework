<!-- <template>
    <div class="new-auction">
        <br>
        <h2>TEST</h2>
    </div>

    <div class="border rounded bg-light shadow p-4">
    <form id='upload_form' method='POST' action="{% url 'http://localhost:8000/mainapp/api/items/' %}" enctype='multipart/form-data'>
        <div class='form-group'>
            <textarea class="form-control" name='text' rows='4'>{{ profile.text }}</textarea>
            <input type="file" id="img_file" style="display:none;">
            <button type='submit' class="btn btn-primary mt-3">Save</button>
        </div>
    </form>
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

    methods:{
        $(function () {
            // connecting click on profile image with click on upload file button
            $('#profile-img').click(function() {
                console.log('Uploading image...')
                $("#img_file").click()
            });

            $('#img_file').change(function uploadFile() {
                var formdata = new FormData()
                var file = document.getElementById('img_file').files[0]
                formdata.append('img_file', file)
                formdata.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val())
                $.ajax({
                    type : 'POST',
                    url  : "{% url 'mainapp:uploadimage api' %}",
                    data : formdata,
                    success: function(data) {
                        $('#profile-img').attr("src",data);
                    },
                    processData : false,
                    contentType : false,
                })
            })
        })
    }
}


</script> -->
<template></template>
<script></script>