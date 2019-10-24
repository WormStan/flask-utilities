$('#bs_table_demo').bootstrapTable({
    columns: [{
        field: 'string_col',
        title: 'string_col',
        sortable: true,
        filterControl: 'input'

    }, {
        field: 'bool_col',
        title: 'bool_col',
        filterControl: 'select'

    }, {
        field: 'content_col',
        title: 'content_col',
        sortable: true,
        filterControl: 'select'
    }, {
        field: 'datetime_col',
        title: 'datetime_col',
        sortable: true,
        filterControl: 'select'
    }],
    showColumns: true,
    //Data Source URL, remote rest api
    url: 'http://127.0.0.1:5001/DataBaseApi',
    //Pagination
    sidePagination: 'client',
    pagination: true,
    pageList: [10, 20, 50, 'all'],
    //Search
    search: true,
    //Export
    showExport: true,
    exportDataType: 'all',
    //Show refresh button
    showRefresh: true,
    //Filter
    filterControl: true,
    //Multi Sort
    showMultiSort: true,
})