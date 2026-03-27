function getCookie(name){
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
}
function loadPage(context){
    const role = context.role;
    alert(role + ' ' + JSON.stringify(context));
    // Exemplu utilizare:
    document.querySelector('h1').textContent += ` (User: ${context.user_username}, Role: ${role})`;
}
document.addEventListener('DOMContentLoaded', () => {
    if (window.pageContext) {
        loadPage(window.pageContext);
    } else {
        console.error('Context lipsă!');
    }
});