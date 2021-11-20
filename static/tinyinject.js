var script = document.createElement('script')

script.type = 'text/javascript'

script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js"

document.head.appendChild(script)

script.onload = function () {
  for (let i = 1; i <= 3; i++) {
    tinymce.init({
      selector: #id_desc'+i+' 
    });
  }
}
