var todo = new Vue({
    el: '#todo',
    data: {
        title: '',
        detail: ''
    },
    methods: {
        add: function (event) {
            apiAddTodo({'title' : this.title, 'detail' : this.detail}).then(res => {
                location.href = '/' + cookieUsername() + '/todos';
            });
        }
    }
})
