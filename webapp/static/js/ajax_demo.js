$(function() {
    var options = {
        type: "GET",
        url: "http://127.0.0.1:5001/DataBaseApi",
        dataType: "json",
        async: true,
        success: function(data) {
            $('#bs_table_demo').bootstrapTable("load", data);
        }
    }
    $.ajax(options);
});