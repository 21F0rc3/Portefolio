var vm = new Vue({
    delimiters : ['[[', ']]'],
    el: '#crud_page',
    data: {
      model: 'Project'
    }
});

function editRow(elem, table_headers) {
  var tr = $(elem).parent();
  
  var editFormDiv = $("#editForm");
  editFormDiv.show();
  var editForm = editFormDiv.find("form");

  $(document).ready(function() {
    var i=0;
    
    table_headers.forEach(header => {
      if(editForm.children().eq(i).is("select")) {
        editForm.children().eq(i).val(tr.children().eq(i).html());
      }else{
        editForm.children().eq(i).find("input").val(tr.children().eq(i).html());
      }

      i++;
    });
  });

}