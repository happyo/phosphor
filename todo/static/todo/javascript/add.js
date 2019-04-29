var todo = new Vue({
    el: '#todo',
    data: {
        title: '',
        detail: ''
    },
    methods: {
        add: function (event) {
            if (this.title.length == 0) {
                vant.Toast('名称不能为空');
            } else {
                apiAddTodo({'title' : this.title, 'detail' : this.detail}).then(res => {
                    location.href = '/' + cookieUsername() + '/todos';
                });
            }
        }
    }
})
