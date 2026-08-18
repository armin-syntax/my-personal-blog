document.addEventListener('DOMContentLoaded', function() {
  const postBody = document.getElementById('postBody');

  if (postBody) {
    const links = postBody.getElementsByTagName('a');

    for (let i = 0; i < links.length; i++) {
      links[i].setAttribute('target', '_blank');
    }
  }
});
