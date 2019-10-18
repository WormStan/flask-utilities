$('#bs_table_demo').bootstrapTable({
    columns: [{
        field: 'string_col',
        title: 'string_col'
    }, {
        field: 'bool_col',
        title: 'bool_col'
    }, {
        field: 'content_col',
        title: 'content_col'
    }, {
        field: 'datetime_col',
        title: 'datetime_col'
    }],
    'search': true,
})

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