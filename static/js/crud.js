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

  var i=0;
  table_headers.forEach(header => {
    editForm.children().eq(i).find("input").val(tr.children().eq(i++).html())
  });
}