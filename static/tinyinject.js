var script = document.createElement('script')

script.type = 'text/javascript'

script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js"

document.head.appendChild(script)

script.onload(function name() {
  tinymce.init({
      selector: '#id_desc1'
    });
})

// for (let index = 1; index < 4; index++) {
    
//     tinymce.init({
//         selector: '#id_desc1'
//       }); 
    
// }