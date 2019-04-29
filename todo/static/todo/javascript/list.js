var list = new Vue({
    el: '#list',
    data: {
        items: [],
        loading: false,
        finished: false
    },

    mounted() {
        apiTodoList().then(res => {
            this.items = res['data']['items'];
        });
    },

    methods: {
        signOut: function (event) {
            apiSignOut().then(res => {
                location.href = '/login';
            });
        },
        addItem: function (event) {
            var href = location.href;
            location.href = '/' + cookieUsername() + '/todos/new';
        },
        editItem: function (todoId) {
            location.href = '/' + cookieUsername() + '/todos/' + todoId + '/';
        },
        finishItem: function (todoId) {
            apiFifishTodo(todoId, {'status' : 1}).then(res => {
                location.reload();
            });
        },
        deleteItem: function (todoId) {
            apiDeleteTodo(todoId).then(res => {
                location.reload();
            });
        },
        fetchData: function () {
            apiTodoList().then(res => {
                this.items = res['data']['items'];
                this.loading = false;
                this.finished = true;
            });
        }
    }
});
