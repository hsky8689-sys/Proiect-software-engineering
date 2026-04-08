var djangoContext = window.djangoContext
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
    const domains_div = document.getElementsByClassName("project-domains");
}
async function goToMainProjectPage(project_name){
    const desiredUrl = `/projects/project-page/${project_name}/`;
    const bailoutUrl = location.href;
    try{
        const response = await fetch(desiredUrl,{
            headers : {'X-Requested-With': 'XMLHttpRequest'}
        });
         if (response.ok) {
            location.href = desiredUrl;
        } else {
            alert('Nu ai permisiunea sau pagina nu există.');
        }
    }catch (error){
        alert('Couldnt load project page');
        location.href = bailoutUrl;
    }
}
async function goToProjectMembersPage(project_name){
    const desiredUrl = `/projects/project-page/${project_name}/project-members/`;
    const bailoutUrl = location.href;
    try {
        const response = await fetch(desiredUrl, {
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
        });
        if (response.ok) {
            location.href = desiredUrl;
        } else {
            alert('Nu ai permisiunea sau pagina nu există.');
        }
    } catch (error) {
        alert('Eroare de conexiune!');
        location.href = bailoutUrl;
    }
}
async function goToProjectSettings(project_name){
    const desiredUrl = `/projects/project-page/${project_name}/settings/`;
    const bailoutUrl = location.href;
    try{
        const response = await fetch(desiredUrl, {
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
        });
        if (response.ok) {
            location.href = desiredUrl;
        } else {
            alert('Nu ai permisiunea sau pagina nu există.');
        }
    }
    catch (err){
        location.href=bailoutUrl;
    }
}
async function copyLinkToClipboard(){
    try{
        await navigator.clipboard.writeText(window.location.href);
        alert(`Link copied to clipboard`);
    }catch(err){
        console.error(`Fail to copy:`,err);
    }
}
document.addEventListener('DOMContentLoaded', () => {
    if (window.pageContext) {
        loadPage(window.pageContext);
    } else {
        console.error('Context lipsă!');
    }
});
const permission_denied = 'You do not have the permission to access this section';
async function loadTaskSection(){

}
async function loadRolesSection(){
    if(djangoContext.permissions.can_modify_tasks){
        alert(permission_denied);
    }
}
async function loadProjectStatsSection(){
    try{
        <input type="radio">Open for requests</input>
    }catch (err){
        alert(err);
    }
}