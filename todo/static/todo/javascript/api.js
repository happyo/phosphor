const apiTodoList = _ => get('', {});
const apiFifishTodo = (todoId, p) => put('/' + cookieUsername() + '/todos/' + todoId + '/', p);
const apiDeleteTodo = todoId => apiDelete('/' + cookieUsername() + '/todos/' + todoId + '/');
const apiEditTodo = p => put('', p);
const apiTodoDetail = _ => get('', {});
const apiAddTodo = p => post('/' + cookieUsername() + '/todos', p);

function cookieUsername() {
    return Cookies.get('username');
}
