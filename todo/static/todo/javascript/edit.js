var todo = new Vue({
    el: '#todo',
    data: {
        title: '',
        detail: ''
    },
    mounted () {
        apiTodoDetail().then(res => {
            this.title = res['data']['item']['title'];
            this.detail = res['data']['item']['detail'];
        });
    },
    methods: {
        edit: function (event) {
            if (this.title.length == 0) {
                vant.Toast('名称不能为空');
            } else {
                apiEditTodo({'title' : this.title, 'detail' : this.detail}).then(res => {
                    location.href = '/' + cookieUsername() + '/todos';
                });
            }
        }
    }
})
